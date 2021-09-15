# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:16:48 2021

@author: USER
"""
# Tipos de colecciones

# Listas o vectores
# Tipo de dato mutable y ordenado

a = [2, 3, 4]
b = [2, True, 'Hola', 3.4]
c = [2, [3, 4], ['Hola', 'mundo'], [2.3, [2.4, 2.5], 2.6]]

for valor in a:
    print(valor)

for valor in b:
    print(valor)

for valor in c:
    print(valor)

a[0] = 7
print(b[2])
print(c[2][1])
print(c[3][1][1])

a.append(5)  # Agrega el elemento al final de la lista
a.remove(3)  # Elimina el elemento que coincida con el valor
a.pop()  # Elimina el último elemento del vector
a.pop(2)  # Elimina un elemento por posición
a.clear()  # Elimina todos los elementos del vector
# del a
4 in a  # Busca el emento 4 dentro de a
len(a)  # Cantidad de elementos del vector
a = b  # Asignación de b en el mismo espacio de memoria de a
id(a)  # Convierte a decimal la dirección en memoria de un objeto
a = b.copy()  # Copia los elementos de b en a
a = b[:]
b = a[0:3]
b = a[:6]
b = a[2:]

# Tuplas
# Tipo de dato INMUTABLE y ordenado

a = (1, 2, 3, 4)
a = ()
print(a[1])
a = (2, 3, 4)
b = (2, True, 'Hola', 3.4)
c = (2, [3, 4], ['Hola', 'Mundo'], [2.3, [2.4, 2.5], 2.6])
4 in a


# Set
# Mutable pero NO ordenado

a = {1, 2, 3, 4}
a = set()
print(a[1])
b = {2, True, 'Hola', 3.4}
# No permite arrays en su interior
c = {2, [3, 4], ['Hola', 'Mundo'], [2.3, [2.4, 2.5], 2.6]}
4 in a

# Diccionario
# Mutable y No ordenado
a = {}
a = {'nombre': 'Jesús', 'apellido': 'Páez'}
a = {1: 'Jesús', 2: 'Páez'}

a['nombre']


for valor in a:
    print(valor)

for valor in a.values():
    print(valor)

for valor in a.keys():
    print(valor)

for valor in a.items():
    print(valor)

for llave, valor in a.items():
    print(f'Llave: {llave}, Valor: {valor}')

# Funciones

def nombre_funcion():
    pass


def saludar():
    print('Hola Mundo')


def saludar(nombre):
    print(f'Hola {nombre}')


# Python no permite la Sobrecarga de métodos

# Parámetros Opcionales
    
def saludar(nombre = 'Mundo'):
    print(f'Hola {nombre}')

def saludar(nombre, apellido=""):
    print(f'Hola {nombre} {apellido}')

def saludar(nombre= "Mundo", apellido=""):
    print(f'Hola {nombre} {apellido}')

# NO puedo tener un parámetro obligatorio después de un
# parámetro opcional
def saludar(nombre, apellido="", segundo_apellido):
    print(f'Hola {nombre} {apellido}')

# Parámetros ilimitados

def saludar(*nombres):
        print(f'Hola {nombres}')


def saludar(*nombres):
    for nombre in nombres:
        print(f'Hola {nombre}')


def saludar(*nombres, apellido=""):
    for nombre in nombres:
        print(f'Hola {nombre}')
    print(f'Apellido {apellido}')


def saludar(*nombres, apellido):
    for nombre in nombres:
        print(f'Hola {nombre}')
    print(f'Apellido {apellido}')


def saludar(**nombres):
    print(nombres)

def resta(a, b):
    print(a - b)

def operaciones(a, b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = a / b
    return suma, resta, mult, div

resultados  = operaciones(4, 5)

suma, res, mul, div = operaciones(4, 5)

suma, _, _, div = operaciones(4, 5)

# while(condicion):
