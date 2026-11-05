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