#---------------Crear una lista de diccionarios---------------
#Como el título lo dice, es posible crear una lista (una variable, lugar, espacio donde guardas int, float, más listas, str ) pero una lista
#que contenga diccionarios (keys y su value), es decir (nombres y su definición):
"""
PERSONAJES DE HOGWARTS

+---+----------+------------+----------------------+
|   | name     | house      | patronus             |
+---+----------+------------+----------------------+
| 0 | Hermione | Gryffindor | Otter                |
| 1 | Harry    | Gryffindor | Stag                 |
| 2 | Ron      | Gryffindor | Jack Russell terrier |
| 3 | Draco    | Slytherin  |                      |
+---+----------+------------+----------------------+
"""
def main1():
    students = [
        {"name" : "Hermione", "house": "Gryffindor", "patronus": "otter"},
        {"name" : "Harry", "house": "Gryffindor", "patronus" : "stag"},
        {"name": "Ron", "house" : "Gryffindor", "patronus": "Jack Russel Terrier"},
        {"name" : "Draco" , "house": "Slytherin", "patronus" : None }
    ]
    for student in students:
        print(student["name"], student["house"], student["patronus"], sep= ", ")
#como es una lisa, debemos poner comas dentro de los diccionarios y 
#dentro de la lista, es decir cada que termines un {} corchete, (excepto el ultimo).
#Para cuando en una lista no hay value asignado, Python nos ofrece la funcion None
#-----------------------------------------------------------------------------------
#Inculso aunque no entendamos que estamos haciendo, solo debemos entender
#que tenemos una lista ( un lugar donde guardamos varias cosas), en este caso
#la lista guarda diccionarios, que se trata de algo y su definción,
def main2():
    def main():
        spacecraft = {"name": "luis", "age": "20"}
        spacecraft ["heigth"] = "1.85"              #Esta es una manera de agregar más valores a un diccionario
        spacecraft.update({"phrase":"lol","born":"2006"})#Tamben esta .update que permite agregar mas keys, no solo una
        print(create_report(spacecraft))

    def create_report(spacecraft):
        return f"""
        =====REPORT======
        Name: {spacecraft["name"]}
        Age: {spacecraft["age"]}
        Heigth: {spacecraft["heigth"]}
        weigth:{spacecraft.get("weigth", "unknown")}
        =================
        """
        #Con .get podemos acceder tambien a valores de un diccionario y nos permite colocar una palabra en caso de no conocerla.
    main()
#main2()
#IMPORTANTE: Es importante recordar que los valores de la izquierda se llaman keys y las definiciones por así decrilo, values

#Cuando colocas nombre_diccionario[key], imprimes el value, estas accediendo al diciconario a tal key e imprimiendo su value.
#En el caso de usar el .value(), el diccionario[key], no sirve, solo muestra keys no values

#------------.keys()-------------
def main3():
    #creamos un diccionario:
    diccionario = {
        "romeo" : "1.85",
        "julieta" : "1.65",
        "jorge" : "1.78"
    }
    def main():
        for name in diccionario.keys(): #Aquí lo que hace es iterar la variable name en
            print(f"name: {name} is {diccionario[name]} m tall")#diccionario pero solo en las keys, es decir: romeo, julieta, jorge
    main()
#main3()
#Recuerda que cuando colocas diccionario[key], imprimes el value
#Entonces para el for, el name esta cambiando, por lo tanto en la funcion print, también.
#Esto quiere decir que cuando es julieta, name = julieta, entonces el diccionario[name]= diciconario[julieta]
#Lo que va a imprimir el value de julieta que es 1.65 :D.

#-----------.values()--------
def main4():
    #Ahora lo mismo usando .values()
    diccionario = {
        "norma" : "1.65",
        "estefania" : "1.85",
        "Marta" : "1.80"
    }
    def main():
        for heigth in diccionario.values():
            print(f"{heigth} is {convertir_pies(float(heigth))} ft tall")
    def convertir_pies(n):
        return n* 3.28084
    main()
#main4()
#Para este ejemplo, usando .values(), descubrí que no puedes imprimir keys de forma convencional
#entonces solo puedes imprimir los values

#------------ len ----------- Diccionary Methods -----------
#Esta funcion en pocas palabras viene del ingles length que signfica longitud en ingles
#determina la longitud o cantidades de elementos de estructuras de datos como
#listas, cadenas, diccionarios, duplas...

def main5():
    WORDS = {"CHAIR" : "5", "HAIR" : "4", "PAIR" : "4", "GRAPHIC" : "7"}
    def main():
        print("Welcome to spelling bee")
        print("Your letters are: A I P C R H G")

        while len(WORDS) > 0:
            print(f"{len(WORDS)} words left!")
            guess = input("Guess a words: ")

            if guess in WORDS.keys():
                points = WORDS.pop(guess)
                print(f"Good job you scored {points} points!") #Aqui antes en points estaba WORDS[guess], que quitamos por el .pop()
            if guess == "GRAPHIC":
                WORDS.clear()   #limpia todo el diccionario
                print("Congrats you finish the game!")
        print("That´s the game!")
    main()
#main5()

#También añade la función .pop(), .clear(), .items():
#.pop() me regresa el valor de el key y borra la key del diccionario
#es por eso que usamos points = WORDS.pop() para guardar el value
#En este caso el programa funciona porque con .pop le restamos al diccionario items
#como usamos un while, va a llegar un punto en el que WORDS sea cero
#entonces se detiene e imprime mensaje de fin.
#En este programa se ejecutan ambos if, es por eso que imprime points y luego acaba
#Pero si los inviertes, el dicionario borra graphic y ya no es parte de la lista.

def main6():
    WORDS = {"HOLA" : "4", "ADIOS" : "5", "BUENAS" : "6"}
    def main():
        print("Items del diccionario: ")
        for palabra, letras in WORDS.items(): #generalmente se pone keys, values in WORDS.items(), pero
            print(f"{palabra} tiene {letras} letras") #acá por facilidad usamos palabra y letras
    main()
main6()

#items devuelve un par (item) en el formato (key, value)