# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 15:59:28 2021

@author: USER
"""
# Condicionales

# Tablas de verdad

# Tabla del and
# v and v = v
# v and f = f
# f and v = f
# f and f = f
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

# Tabla del or
# v or v = v
# v or f = v
# f or v = v
# f or f = f
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

# Negacion
print(not True)  # False
print(not False)  # True

# Mas de dos condicionales al mismo tiempo
print(True and False and True or False or True or True)  # True
print(True and (False and True) or False or (True or True))  # True

# Jerarquia de operaciones
# 1. Parentesis y llaves
# 2. Potencias y raices
# 3. Multiplicacion y division
# 4. Sumas y restas

# Jerarquia de operaciones booleanas
# 1. Parentesis y llaves
# 2. Tabla de verdad

# Estructura if
x = -1
if (x > 0):
    print('1')
else:
    print('2')

# Haga un algoritmo que dada la edad de una persona, indique si es mayor
# o menor de edad
edad = int(input('Digite la edad de la persona: '))
if(edad >= 18):
    print('Si es mayor de edad')
else:
    print('No es mayor de edad')

# Haga un algoritmo que indique su un estudiante aprobo o reprobo una
# asignatura, teniendo en cuenta que aprieba con minimo una
# calificasion de 3.0 hasta 5.0
nota = float(input('Digite su nota: '))
if(nota >= 3.0 and nota <= 5.0):
    print('Aprobó')
elif(nota < 3.0 and nota > 0):
    print('Reprobó')
else:
    print('La nota ingresada no es válida')

# Haga un algoritmo que diga si un numero es negativo, positivo o cero
numero = float(input('Digite el número: '))
if(numero > 0):
    print('Positivo')
elif(numero < 0):
    print('Negativo')
else:
    print('El número es cero')

# Ciclos

# Ciclo for
for valor in range(11):
    print(valor)

for valor in range(1, 11):
    print(valor)

for valor in range(0, 13, 3):
    print(valor)

for valor in range(11):
    print(valor)
print(valor + 1)

# Haga un algoritmo que reciba N notas de un estudiante y calcule el
# promedio total
cn = int(input('Digite la cantidad de notas: '))
if(cn > 0):
    acumulador = 0
    for x in range(cn):
        nota = float(input(f'Digite la nota {x + 1}: '))
        acumulador = acumulador + nota
    promedio = acumulador / cn
    # Para redondear el resultado
    promedio = round(promedio, 2)
    print(f'El promedio final es: {promedio}')
else:
    print('El numero de notas no puede ser menor o igual a cero')





        

































































