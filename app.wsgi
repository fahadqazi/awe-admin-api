#!/usr/bin/env python                                                                                                                          
# -*- coding: utf-8 -*-                                                                                                                        
# import packages sys and site to control the environment                                                                                      
import sys, site, os, pprint
sys.stdout = sys.stderr
sys.path.insert( 0, os.path.dirname( os.path.realpath( __file__ ) ) )
import local_settings

# set base dir for code and libraries                                                                                                          
config = local_settings.env
sys.path.insert( 1, config.get( 'HOME_DIR' ) )
sys.path.insert( 1, config.get( 'VIRTUALENV_DIR' ) )

# import my code                                                                                                                               
from app import app as application

