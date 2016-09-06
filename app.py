from flask import Flask, render_template, jsonify, request
import json, os, logging, requests
import local_settings
from pymongo import MongoClient
from quiddi.util import logger
from models.theme import Theme
logging.basicConfig()
config = local_settings.env
app = Flask( config.get( 'APPLICATION_NAME', 'polymer-form-api' ))
theme_logger = logging.getLogger('theme')
ql = logger(logger=theme_logger, level=logging.INFO)
uri = "localhost"
client = MongoClient(uri)
db = client['affiliate_website']
collection = db['themes']
theme = Theme(ql, collection)

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

@app.route('/add-theme', methods=['GET','POST'])
def addTheme():
    if request.method == 'POST':
        payload = json.loads(request.data)
        payload.pop('_id', None)
        document_id = theme.add_theme(payload)

        if document_id:
            return json.dumps({"status":"Inserted Successfully"})
    return json.dumps({"status":"Insert unsuccessfull"})
 
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

@app.route('/get-themes', methods=['GET'])
def getThemes():
    response = []
    all_themes = theme.get_themes()
    for site in all_themes:
        site.update({"_id":str(site['_id'])})
        response.append(site)
    return json.dumps(response)    

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

@app.route('/edit-theme', methods=['POST'])
def editTheme():
    payload = json.loads(request.data)
    payload.pop('_id', None)
    doc_id = collection.replace_one({'website.name': payload['website']['name']}, payload).matched_count

    if doc_id:
        return json.dumps({"status":"Edited Successfully"})
    else:
        return json.dumps({"status":"Edit Unsuccessfull"})

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

if __name__ == '__main__':
    pass
else:
    app.root_path = config.get('HOME_DIR')

