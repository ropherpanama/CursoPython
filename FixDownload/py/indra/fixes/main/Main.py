__author__ = 'rospena'

import sys
import time
import configparser as cfp
from py.indra.fixes.commons.Utils import Utilities
from py.indra.fixes.conection.ConectorDB import Connector


class Main(object):
    #Main program
    def __init__(self):
        try:
            c = Connector()
            self.settings = c.get_settings()
            self.source = c.get_source()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    def validate_itiner(self):
        try:
            sql = Utilities.config("DBQueryes", self.settings)['validatesmfrutaperson']
            cursor = self.source.cursor()
            cursor.execute(sql)
            response = str(cursor.fetchone()[0])

            if response.__len__() == 0:
                print("No se encontraron datos para el caso solicitado, \nrevise los parametros de entrada")
            else:
                print("status: " + response)
                if response == '1' or response == '2' or response == '3':
                    print("Estado no determinado")
                else:
                    print(Utilities.config("CodigosDeError", self.settings)[response.lower()])

        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise

    def get_source(self):
        return self.source

    def get_settings(self):
        return self.settings


#Main program
try:
    m = Main()
    m.validate_itiner()
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


