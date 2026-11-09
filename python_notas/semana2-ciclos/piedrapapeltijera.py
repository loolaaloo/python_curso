#--------------------Juego piedra, papel o tijera---------------
#Mientras terminaba el cruso de la semana 2 (ciclos), se me ocurrió que sería una buena idea
#hacer el juego piedra, papel o tijera para practicar condicionales y también ciclos.
#Entonces le pedí a la IA que me redactará el problema:
"""
Reglas:
- Piedra le gana a tijera.
- Tijera le gana a papel.
- Papel le gana a piedra.
- Si ambos eligen lo mismo, es empate.

Versión 1: una sola ronda
1. Pedir al jugador que escriba piedra, papel o tijera.
2. La computadora elige una opción al azar (random.choice).
3. Comparar las dos jugadas y mostrar quién ganó, o si fue empate.

Versión 2: validar
- Si el jugador escribe otra cosa, mostrar "Opción no válida".

Versión 3: ciclos
- Repetir el juego con un while hasta que el jugador escriba "salir".

Versión 4 (opcional): marcador
- Llevar la cuenta de victorias del jugador y de la computadora.

---Conforme vaya redactando el programa iré subienod de dificultad, por lo que el código final
---solo será la versión final. 
"""
import random
def main():
    victorias_jugador = 0
    victorias_computadora = 0
    while True:
        opciones = ["piedra", "papel", "tijera"]
        computadora = random.choice(opciones)
        #pedir usuario entrada:
        jugada = input("Piedra, papel o tijera: ").lower().strip()
        #comprobar entrada y verificarla correcta:
        if jugada in opciones:
            print("Rival: ", computadora)
            punto = ganador(jugada,computadora)
            if punto == "humano":
                victorias_jugador +=1
            elif punto == "computadora":
                victorias_computadora +=1
            print(f"\n------jugador: {victorias_jugador} ----computadora: {victorias_computadora}")
            conidicon = seguir()
            if not conidicon == True:
                break
            elif conidicon == False:
                print("Opción inválida...")
        else:
            print("Opción inválida...")
#Condicionales:
def ganador(jugador,rival):
    if jugador == "piedra" and rival == "papel":
        print("Perdiste :C...")
        return "computadora"
    elif jugador == "piedra" and rival== "tijera":
        print("Ganaste :D...")
        return "humano"
    elif jugador == "tijera" and rival == "papel":
        print("Ganaste :D...")
        return "humano"
    elif jugador == "tijera" and rival == "piedra":
        print("Perdiste :C...")
        return "computadora"
    elif jugador == "papel" and rival == "tijera":
        print("Perdiste :C...")
        return "computadora"
    elif jugador == "papel" and rival == "piedra":
        print("Ganaste :D...")
        return "humano"
    else:
        print("Empate")
def seguir():
    decision = input("¿Deseas seguir jugando?: ").lower().strip()
    return decision == "si"
main()
