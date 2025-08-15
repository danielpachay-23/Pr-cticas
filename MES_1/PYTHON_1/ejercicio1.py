def hello():
    return "hello world!!"



print(hello())
print("1,2,3,4,5,6")

"""
EJERCICIO 1
Pide al usuario su nombre, edad y ciudad. Luego imprime un mensaje como:
Hola Juan, tienes 20 años y vives en Quito.
"""
nombre = input("Por favor, indique su nombre: ")
edad = int(input("Por favor, indique su edad: "))
ciudad =  input("Por favor indique su ciudad de origen: ")

#versión 1
# print ("Me llamo "+nombre+", y tengo "+str(edad)+" años y vivo en la ciudad de "+ciudad)

#Versión mejorada
if edad >= 0:
    print(f"Me llamo {nombre}, y tengo {edad} años y vivo en la ciudad de {ciudad}")
else:
    print ("Vuelva a colocar un valor numérico que sea mayor igual que 0")


"""
Ejercicio 2
Pide dos números y muestra:
La suma
La resta
La multiplicación
La división
"""

num1 = int(input("Por favor, registre el primer valor numérico: "))
num2 = int(input("Por favor, registre el segundo valor numérico: "))

print(f"La suma de {num1} y {num2} es: {num1+num2}")
print(f"La resta de {num1} y {num2} es: {num1-num2}")
print(f"La multiplicación de {num1} y {num2} es: {num1*num2}")

if num2 != 0: 
    print(f"La división de {num1} y {num2} es: {num1/num2}")
else: 
    print("No se puede dividir entre ceros")

#Ejercicio de variables de memoria
"""
Crea una variable a = 5 y otra b = a.
Cambia a a 10.
Imprime a y b.
Luego, haz lo mismo con una lista lista1 = [1,2,3] y lista2 = lista1, añade un elemento y observa qué pasa.
"""

a = 5; b = a
a= 10
print(f"a = {a}, b = {b}")

list1 = [1,2,3] ; list2 = list1
list1.append(4)

print(f"Lista es igual a {list1}")
print(f"Lista2 es igual a {list2}")

import copy
list3 = copy.deepcopy(list1)
list1.append(5)
print(list1)  # [1,2,3,4,5]
print(list3)  # [1,2,3,4] → no se modificó
