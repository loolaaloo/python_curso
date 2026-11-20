#------ Ejercicios para reforzar los ciclos-----
#Todavía sentí que me faltaba más ejercicios para reforzar este tema de los ciclos
#por este motivo le pedí a la IA dos ejercicios más.
"""
--- Ejercicio A: pide contraseña ---
Define una contraseña dentro del programa (por ejemplo "python123").
El programa pide la contraseña hasta que el usuario acierte.
Al final, muestra en cuántos intentos lo logró.

Ejemplo:
    Contraseña: hola
    Incorrecta...
    Contraseña: python
    Incorrecta...
    Contraseña: python123
    ¡Acceso concedido en 3 intentos!

Pistas:
- Antes de programar, responde las tres preguntas:
    1. ¿Qué se repite?
    2. ¿Cuándo se detiene?
    3. ¿Qué debe recordar entre vueltas?
- Un solo while True, con break al acertar.
- El contador de intentos va ANTES del ciclo.
- El mensaje final va después del ciclo (o justo antes del break).

--- Ejercicio B: menú repetido ---
Un menú que se repite hasta que el usuario elija salir:

    1) Saludar
    2) Despedirse
    3) Salir

- Opción 1: imprime un saludo.
- Opción 2: imprime una despedida.
- Opción 3: termina el programa.
- Cualquier otra cosa: "Opción inválida".

Pistas:
- Un solo while True. NO llames a main() dentro del ciclo.
- Usa match/case o if/elif, el que prefieras.
- El break solo se ejecuta en la opción 3.
- Las opciones se comparan como texto ("1", "2", "3"), porque
  input() devuelve texto. Así evitas que falle si escriben letras.
"""
#Ejercicio A:
"""
Yo quise mejorar un poco el código solicitando al usuario una contraseña.
1.Se repite el ciclo para pedir una contraseña válida y verificarla
2.Se detiene cuando es correcta
3.Debe recordar la entrada del usuario.
"""
def mainA():
    def solicitar_contraseña(c, d):
        while True:
            d +=1
            contraseña = input("Ingrese la contraseña: ")
            if contraseña == c:
                break
            print("incorrecta...")
        print(f"contraseña válida, con {d} intentos...")

    def programa():
        while True:
            contraseña_valida = input("Dame una contraseña: ")
            contraseña_contador = 0
            solicitar_contraseña(contraseña_valida, contraseña_contador)
            respuesta = input("¿Desea repetir el sistema?: ").lower().strip()
            if respuesta == "no":
                break
    programa()
#mainA()

#Ejercicio B:
"""
1. Se repite el menu
2. Se detiene cuando el usuario escribe 3
3. No debe recordar nada entre vueltas
"""

def mainB():
    def menu():
        while True:
            print("""1) Saludar
2) Despedirse
3) Salir""", end="\n\n")
            eleccion = input("Elija una opción (1,2,3): ")
            match eleccion:
                case "1":
                    print("Hola...", end="\n\n")
                case "2":
                    print("Adiós...", end="\n\n")
                case "3":
                    break
                case _:
                    print("opción inválida...")
                    break
    menu()
mainB()
