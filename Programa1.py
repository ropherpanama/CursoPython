#Mi primer programa Python
#El print recibe cualquier cantidad de parametros separados por coma (,)
#incluyendo expresiones aritmeticas como se muestra a continuacion.
#Si se abre con IDLE, ejecutar con la tecla F5

print ("Si sumas 2 + 3 el resultdo es ",
       2 + 3,
       "\nPero si los restas el resultado es ",
       2 - 3,
       "\nQue cosa no?")

#Variables
#No necesitan declarar de que tipo son, solo se declaran (tipo dinamico)
a = "Soy una cadena de texto"
b = 50
c = 25

print(a, "\nOperacion:", b + c)

c = "Cambien de tipo de dato ... "
print(c)

multilinea = """ Esto es cool
                 puedo escribir lineas sin usar carracteres de escape
                 solamente usando las comillas triples :)"""

print(multilinea) 

#Las cadenas tambien aceptan operaciones aritmeticas

d = "eco"
e = d * 3
f = "sistema"
print("Multiplicacion de cadenas:", e)

e = d + f
print("Suma de cadenas:", e)
