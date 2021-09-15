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
