#Mi quinto programa Python
#Si se abre con IDLE, ejecutar con la tecla F5
#Clases
#El metodo __init funciona como inicializador, siempre se le debe pasar el
#argumento self, en este y en todas las funciones que se
#declaren en la clase, si no el error motrado es este:
#TypeError: function() takes 0 positional arguments but 1 was given

class Archivo:
    def __init__(self, name, content):
        self.name = name
        self.content = content
        print("Archivo llamado ", name)

#Las funciones "privadas" inician con __ (doble subrayado)
    def __escribir(self):
        t = input("Escriba > ")
        self.content += "\n" + t

    def leer(self):
        if len(self.content) == 0:
            print("Archivo no tiene contenido, escriba algo")
        else:
            print("cat " + self.name + "\n",self.content)


#Uso de la clase

a = Archivo("CV.doc", "")
print("""Escriba:
    e para escribir
    l para leer
    bye para salir""")
    
while True:
    r = input("> ")
    if r == "bye":
        print("Adios")
        break
    elif r == "e":
        a._Archivo__escribir()#Llamado a una funcion privada
    elif r == "l":
        a.leer()
    else:
        print("Opcion no valida")
              
          
