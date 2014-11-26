#Mi segundo programa Python
#Si se abre con IDLE, ejecutar con la tecla F5

#Listas (arrays o vectores)
lista1 = [1, 2, "tres", 4, "cinco", [2,3], 7, "ocho", "nueve", 10]

print("Accediendo a la lista:", lista1[2])
#La sublista esta en el index 5 de la lista principal, accedemos al primer valor
#de ella (sublista)
print("Accediendo a la sublista:", lista1[5][0])

print("Lista original:", lista1)
lista1[0] = 100
print("Modifico 1er elemento (1 por 100):", lista1)

#Uso de numero negativo (busqueda inversa)
#Buscará la 3 posicion de atras hacia adelante de la lista
print(lista1[-3])

#Uso de Slicing (particionado) o busqueda por rango
print(lista1[0:4])

#Uso de saltos (cada n cantidad)
#Buscara solo en la posicion 0 a la 8, saltando 3 elementos en cada item encontrado
print(lista1[0:8:3])

#Tuplas
#Se pueden manejar a las listas
#La gran diferencia es que las tuplas son inmutables
#tupla1[1] = 100 (TypeError: 'tuple' object does not support item assignment)
tupla1 = (1,2,3,4,5)
print("Tupla:", tupla1[:3])

#Diccionarios, la misma vaina que los HashMaps de JAVA :)
diccionario = {"uno":1, "dos":2, "tres":3}
print("Diccionario:", diccionario["uno"])
