"""
Ejercicios prácticos
--- Consejo de ingeniero: en programación, piensa en pasos lógicos antes de escribir el código. Primero el qué, después el cómo.
"""

# Ejercicio 1  Condicional
# Escribe un programa que pida un número al usuario e indique si es positivo, negativo o cero.
print("Ejercicio 1  Condicional")
num = int(input("Ingrese un valor: "))
if num > 0:
    print(f"El valor de {num} es positivo")
elif num < 0:
    print(f"El valor de {num} es negativo")
else:
    print(f"El valor de {num} es cero")

# Ejercicio 2  Bucle for
# Muestra la tabla de multiplicar de un número que pida al usuario.
print("\nEjercicio 2  Bucle for")

def multiplicar(a): 
    for i in range(13):
        print(f"{num2} multiplicado por {i} es igual a {num2*i}")
        
num2 = int(input("Ingrese una valor para Multiplicar: "))
multiplicar(num2)

# Ejercicio 3  Bucle while
# Haz un contador que empiece en 10 y vaya bajando hasta 1
print("\nEjercicio 3  Bucle while")
cont = 10
while cont >=1:
    print(f"Contador: {cont}")
    cont -= 1