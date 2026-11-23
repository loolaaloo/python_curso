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
main4()
#Para este ejemplo, usando .values(), descubrí que no puedes imprimir keys de forma convencional
#entonces solo puedes imprimir los values