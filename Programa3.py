#Mi tercer programa Python
#Si se abre con IDLE, ejecutar con la tecla F5

#Sentencias de flujo

#IF
a = 10
b = 70

#Importante: las sentencias a ejecutar segun se cumpla la condicion o no; debe
#identarse con un Tab
if (b/a) > 5 :
    print("Alcanza para todos")
    print("tenemos", 70/10)
else:
    print("No alcanza para todos")

#WHILE
#Se pueden omitir los parentesis de la condicion
count = 0

print("Uso del while")
while ( count <= 5 ):
    count += 1
    print("Imprimo " + str(count) + " veces")

#Entrada por teclado con input(""),
#en Python 3 se elimino el raw_input()
    
print ("While infinito, escribe adios para salir")

while True:
    entrada = input("> ")
    if entrada == "adios":
        break
    else:
        print (entrada)

#FOR
#Similar a Java se puede iterar sobre objetos sin necesidad de un contador
        
secuencia = ["uno","dos","tres","cuatro","cinco"]

for e in secuencia:
    print("Salgo en " + e)
