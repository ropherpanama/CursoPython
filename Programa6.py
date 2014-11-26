#Mi sexto programa Python
#Si se abre con IDLE, ejecutar con la tecla F5

#Conexion a base de datos Oracle
#Instalar el modulo cx_Oracle, si no; no sirve (http://cx-oracle.sourceforge.net/)
#version segun version de Python, para este se instalo 3.3 por usar Python 3.3.2

import cx_Oracle as ora
import time

db = ora.makedsn('10.240.197.191', 1521, 'facsitiodes')
source = ora.connect('FACSITIO','FACSITIO', db)
print(source.version)
initial = time.time()
cursor = source.cursor()
#cursor.execute('select * from smf where rownum < 20')
cursor.execute('select * from ciclos_itin')
res = cursor.fetchall() #Lo devuelve como tupla

#Creacion de archivo (nombre, modo)
file = open("tableres.txt", "w")

for element in res:
    file.write(str(element) + "\n") #Imprime tuplas

#for element in cursor:
#    file.write(str(element) + "\n")

file.close()
    
elapsed = (time.time() - initial)
print(elapsed, " seconds")
cursor.close()
source.close()

