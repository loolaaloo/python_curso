#-----------Pruebas de programas--------------
#Aquí coloco algunos programas que fuí realizando para experimentar y aprender, no estan relacionados con 
#el tema de la subcarpeta, pero son de utilidad para el aprendizaje.

#A diferencia de las funciones (print, def, input, return...etc.)
#He aprendido que los condicionales y los ciclos no son funciones son llamados "keywords":
"""
No se puede usar como nombre de variable, función ni ningún otro identificador. 
No se importa: siempre está disponible.
No se puede reasignar ni "sobrescribir".
Python 3.13 tiene 35 keywords + 4 soft keywords (como match, case). Puedes verlas todas con:
"""
def main():
    from keyword import kwlist
    print(kwlist)
main()
#Por ejemplo match  y case son soft-keywords.
def main1():
    i = 0
    while i != 3:
        i += 1
        print("meow")
main1()

#--------------range-------
#si colocamos:
def main2():
    for i in range(2):
        print("blablabla")
main2()
#range(stop), por defecto cuenta de 1 a 2, entonces ejecutará dos veces el bloque de código
"""
Pero también:
range(start,stop) ----> indica donde empieza y donde termina
range(start,stop,step)-----> indica donde empieza, donde termina y de cuanto en cuanto
"""
#Ejemplo:
def main3():
    for _ in range(3,20,4):
        print("hola")
main3() #lo esperado es que imprima 5 veces hola

def main4():
    print("meow\n"*3, end="")
#impirmir meow 3 veces con enters y sin ese enter del final que se ve feo, es una forma de hacerlo correta
#sin embargo, esta forma otros lenguajes no lo tienen
