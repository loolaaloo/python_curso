#-----------------EJERCICIOS DE CICLOS----------------------------
#Le pedí a la IA un par de ejercicios para prácticar el uso de ciclos (while-for):
#Todo lo realizó yo, las respuestas adjuntas son propias, no resueltó por la IA, sólo como herramienta.
"""
EJERCICIOS DE CICLOS

--- Nivel 1: for y range ---
1. Imprime los números del 1 al 10, cada uno en su línea.
2. Imprime los números pares del 2 al 20.
3. Imprime una cuenta regresiva del 10 al 1 y al final "¡Despegue!".

--- Nivel 2: acumuladores ---
4. Suma los números del 1 al 100 y muestra el resultado.
   (Pista: crea una variable en 0 ANTES del ciclo y súmale en cada vuelta.)
5. Pide un número n y calcula su factorial (n! = 1 * 2 * 3 * ... * n).
6. Pide un número y muestra su tabla de multiplicar del 1 al 10.

--- Nivel 3: while ---
7. Pide números al usuario hasta que escriba 0, y al final
   muestra cuántos números escribió y cuánto suman.
8. Adivina el número: el programa elige un número del 1 al 100 al azar
   y le pide al usuario que lo adivine. Después de cada intento dice
   "Más alto" o "Más bajo". Al acertar, muestra en cuántos intentos lo logró.
   (Pista: while + random.randint(1, 100) + un contador de intentos.)

--- Nivel 4: ciclos anidados ---
9. Imprime un triángulo de tamaño n:
   #
   ##
   ###
   ####
   (Pista: la cantidad de # de cada fila depende de i.)
10. Imprime las tablas de multiplicar del 1 al 5 completas.

--- Reto final ---
11. Pide un número y di si es primo.
    (Pista: un número es primo si ningún número entre 2 y n-1 lo divide
    exacto. Piensa en usar % dentro de un for, y en una variable bool.)
"""
#-.-.-.-.-.-.NIVEL 1:.-.-.-.-.-.-
#1.-
def main1():
    for i in range(1,11):
        print(i)
#2.-
def main2():
    for i in range(2,22,2):
        print(i)
#3.-
def main3():
    for i in range(10,0,-1):
        print(i)
    print("¡Despegue!")

#-.-.-.-.-Nivel 2:.-.-.-.-.-.
#1.-
def main4():
    contador = 0
    for i in range(1,101):
        contador += i
    print(contador)

#2.-
def main5():
    def main():
        numero = int(input("Número para calcular factorial: "))
        respuesta = factorial(numero)
        imprimir_respuesta(respuesta)
    def factorial(n):
        resultado = 1
        for i in range(1,n+1):
            resultado *= i
        return resultado
    def imprimir_respuesta(r):
        print(r)
    main()

#3.-
def main6():
    while True:
        numero = int(input("Número para calcular su tabla de multiplicar: "))
        for i in range(1, 11):
            print(f"{i}*{numero} = {i*numero}")
        respuesta = input("¿Deseas calcular otro? ").lower().strip()
        if respuesta == "no":
            break
main6()
#En este programa aprendi que no es necesario colocar un else, porque en caso de que sea si, el ciclo while se 
#repite indefinidamente, solo queremos deternerlo si es no. También es mejor si colcoas así la conidción:
#if respuesta != "si": break, porque solo queremos que haga break son si

#.-.-.-.-.-.-.-.-.-Nivel 3.-.-.-.-.-.-.-.-.-
#1.-
