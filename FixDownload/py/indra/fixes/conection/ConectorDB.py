from socket import socket

__author__ = 'rospena'

import cx_Oracle as ora
import configparser as cfp
import sys
import time
from py.indra.fixes.commons.Utils import Utilities
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

#To give value to an global variable use the self operator, then you will be able to use
#getters and setters
class Connector(object):

    def __init__(self):
        try:
            self.settings = cfp.ConfigParser()
            self.settings._interpolation = cfp.ExtendedInterpolation()
            self.settings.read('D:/resources/db_settings.ini')
            self.settings.sections()

            ip_server = Utilities.config("DBParameters", self.settings)['ipaddress']
            port = Utilities.config("DBParameters", self.settings)['port']
            sid = Utilities.config("DBParameters", self.settings)['dbsid']
            user = Utilities.config("DBParameters", self.settings)['dbuser']
            password = Utilities.config("DBParameters", self.settings)['dbpass']

            db = ora.makedsn(ip_server, port, sid)
            self.source = ora.connect(user, password, db)
            print("Ready", self.source.version)

        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    def get_source(self):
        # print("getting de source object", self.source)
        return self.source

    def get_settings(self):
        # print("getting de settings object", self.settings)
        return self.settings