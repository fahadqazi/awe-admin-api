from flask import Flask, render_template, request, make_response
from jinja2 import Environment, PackageLoader
from raven import Client
from quiddi.util import logger, send
from datetime import datetime, timedelta
import logging

logging.basicConfig()

class Theme:

    def __init__(self, logger, collection):
        self.ql = logger
        self.collection = collection
        self.search_key = "website.name"
        self.log("Initialising class", logging.INFO)
        self.log("Current time: %s" % (str(datetime.now())), logging.INFO)

    def log(self, message, level):
        self.ql.log(
            message=message,
            level=level
            )

    def get_payload(self):
        try:
            self.log("getting payload from collection using find_one()", logging.INFO)
            return self.collection.find_one()
        except Exception as e:
            self.log("could not get payload from collection: %s" %(e), logging.ERROR)

    def add_theme(self, doc):
        try:
            result = collection.insert_one(doc)
            self.log("inserted document to collection", logging.INFO)
        except Exception as e:
            self.log("document insert failed: %s" %(e) , logging.ERROR)
        return result

    def find_theme(self, website_name):
        try:
            document = self.collection.find_one( { self.search_key : website_name } )
            return document
        except Exception as e:
            self.log("could not find relevant document in database:  %s" %(e))
