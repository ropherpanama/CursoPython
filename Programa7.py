#Mi septimo programa Python
#Si se abre con IDLE, ejecutar con la tecla F5

#SQLAlchemy

import cx_Oracle as ora
import time
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

db = ora.makedsn('10.240.197.191', 1521, 'facsitiodes')
source = ora.connect('FACSITIO','FACSITIO', db)
print(source.version)
initial = time.time()
cursor = source.cursor()
cursor.execute('select * from ciclos_itin')
res = cursor.fetchall() 
