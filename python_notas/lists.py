#-------------------LISTS PYTHON----------------------
"""
En el vídeo añade otro tipo de dato, las listas...
Listas: Así como en la vida real, se trata de una lista de diferentes tipos de datos (str,bool,float,int)
guardados todos en el mismo lugar o en la misma variable.
TIPOS DE DATOS EN PYTHON:
+---------+--------+-------------------------+------------------------------+
| Tipo    | Nombre | Qué guarda              | Valores posibles             |
+---------+--------+-------------------------+------------------------------+
| Enteros | int    | Números enteros         | Sin límite práctico          |
| Cadenas | str    | Caracteres (texto)      | Caracteres                   |
| Decimal | float  | Números decimales       | Sin límite práctico          |
| Boolean | bool   | Valores de verdad       | True / False (con mayúscula) |
| Listas  | Lists  | Cualquier topo de dato  |str,bool,float,int, otras listas|
+---------+--------+-------------------------+------------------------------+
Para la función is_even, necesitamos devolver (return) un valor (T/F), para que funcione.
"""
#Para ello toma el código que dice meow 3 veces, pero ahora usando for:
#Las listas se usan con [] y dentro el data.
def main():
    for i in [0,1,2]:
        print("meow")
#El código luce más simple, sin embargo, si quieres imprimir 300 meows, tendras que escribir 300 numeros en la lista.
#Muchos en lugar de usar i usan _, como para decir no me importa el nombre de la variable, pero deben poner algo
#porque Python requiere una variable en la que estar sumando.
#Esto se corrige usando una función llamada range(n)


#---------------Ciclo For-------------
#For itera una variable en un rango especifico de datos (litas, tuplas, cadenas o diccionarios)
#iterar: Repetir un bloque de instrucciones hasta cumplir una condición específica
#Aquí a diferencia del while, que solo necesita que sea True ciera condicón, no se itera un bloque de código
#se itera una variable, que en estos ejemplos de más adelante, recorre un conjunto de datos
def main1():
    for i in range(3):
        print("meow")
main()                  #IMPORTANTE: range(n) es una funcion nativa del lenguaje, no requiere ninguna declaración previa

#Aquí hay algo a mejorar, esta "i" en el programa pero nunca la estamos usando, entonces es común ver que se coloca _ (guión bajo).
#range() es una función que define una secuencia numérica
