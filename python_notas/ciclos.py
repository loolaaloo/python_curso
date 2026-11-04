#------------------Ciclos introducción----------------
#Basicamente hablamos de repetir una acción n cantidad de veces
def main():
    print("meow")
    print("meow")
    print("meow")
#main()     #Este código imprime 3 veces "meow", pero si queremos hacelo 30 veces¿? ó 3000¿?
            #se vuelve un mal hábito esxribir n cantidad de veces algo.
            #incluso si quiero cambiar de "Meow" a "woof", no es conveniente 
            #cambiarlo estar cambiando uno por uno.

#-------------While (loop)----------------
#Aquí entra entra un nuevo keyword (while) que su utilidad es estar repitiendo un bloque de código
#una y otra vez. n cantidad de veces como querramos siempre que una condicion sea verdadera (true)
""""
En el vídeo presenta una muy buena explicación tangible.
Decirle a una persona que tengas enfrente (situación hipotética) que diga meow
por cada dedo que bajes, es decir inicias con tres dedos levantados y cada vez que diga meow bajas un dedo
le haces cada vez que diga "meow" la misma pregunta, ¿tengo algun dedo levantado?, si es True, que siga
si es False, que se detenga.
"""
def main1():
    i = 3
    while i != 0:   #expresión booleana (T/F), "SIEMPRE QUE i SEA TRUE HAZ ESTO..."
        print("meow")
#si corro el programa así como esta, es peligroso, impimira "meow" una infinidad de veces
#como nunca cambias el valor de i, estará imprimiendo para siempre
def main2():
    b = 3
    while b != 0:   #expresión booleana (T/F), "SIEMPRE QUE i SEA TRUE HAZ ESTO..."
        print("meow")
        b -= 1
#main2()
#El ciclo while ejecuta una y otra vez el mismo bloque de código hasta que sea falsa la expresión booleana.
def main3():
    i = 1
    while i <= 3:       #otra forma de lógica (aunque son lo mismo)
        print("meow")
        i += 1          #es lo mismo si pones i += 1 antes o después del print.
#main3()                 #puesto que print no necesita de i para funcionar.
#IMPORTANTE Si i = 0 entonces...
""""
En este programa empieza en 1, sin embargo,si empezara en 1, llega a =3, es decir, cuando es 4 (meows) se detiene.
pero en el vídeo se menciona que es mejor establecer como un buen habito siempre emepezar en cero.
y entonces el programa quedaría asi:
"""
def main4():
    i = 0
    while i < 3:
        print("meow")
        i += 1
#main4()                   #lo unico que cambia es el <= a <.
#importante aclarar que si no cambias el <= solo a <, entonces impimira 4 veces el meow, cuentalo con los dedos para comprobarlo.

#----------While, break y continue-----------------
#de esta forma creas un loop inifnito, colocando True, siempre es verdad, pero de alguna manera debes romper ese loop infinito
#es donde usamos break, ademas de continue, ejemplo:
def main5():
    while True:
        n = int(input("What´s n?"))
        if n < 0:
            continue
        else:
            break
    for _ in range(n):
        print("meow")
#main5()
#este programa espera que el usuario ponga un numero entero como n, si es menor a cero, entonces sigue con el loop
#hasta que pone un entero, se detiene (break)
#MUY IMPORTANTE: tal vez es obvio, sin embargo, break y continue solo se pueden usar en un ciclo

#Pero hay una manera, más sencilla:
def main6():
    n = int(input("what´s n?: "))
    while True:
        if n > 0:
            break
    for _ in range(n):
        print("meow")
#main6()

#Ejemplo de programa que pide n (numero), para imprimir meow:
def mainm():
    def main():
        number = get_number()
        meow(number)
    def get_number():
        n = int(input("what´s n? "))
        while True:
            if n > 0:
                break
        return n
    def meow(n):
        for _ in range(n):
            print("meow")
    main()
mainm() #Importante distiguir que usa break pero luego tiene que regresar n (return n), sin embargo, podemos no poner break
#y solo poner return n