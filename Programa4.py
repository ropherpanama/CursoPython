#Mi cuarto programa Python
#Si se abre con IDLE, ejecutar con la tecla F5

#Funciones

#Se define una funcion mediante la palabra def
def calcularEdad (anio_nacimiento):
    print("Tu edad es " + str(2014 - anio_nacimiento) + " años")
    
#Entrada del usuario
entrada = input("Ingrese su año de nacimiento ")

#Llamado de la funcion
calcularEdad(int(entrada))

#Funcion retornando valor
def calcularEdad2 (anio):
    return 2014 - anio

#Llamado de la funcion
entrada2 = input("Ingrese su año de nacimiento ")
answer = calcularEdad2(int(entrada2))
print("Tu edad es " + str(answer) + " años")

#Numero variable de parametros en una funcion
#Puedes usar tuplas o diccionarios para pasar argumentos extras a una funcion

def variable(arg1, arg2, *arg3):
    for s in arg3:
        print("Item: " + str(s))
        
    print(arg1, arg2, arg3)


a = input("Ingrese un numero ")
b = input("otro ...")
c = input("... y otro mas ")

#array = [23,22,21,20] #lista extra
#variable(int(a), int(b), array)
variable(int(a), int(b))

