#---------------Diccionarios----------------
#En el vídeo se define que de igual manera como en la vida real los diciconarios.
#tienen palabras y su definicion, en programación se trata de asociar algo con algo más.
#a diferencia de una lista que se trata solo de una "caja" de varios valores

#ejemplo:
#students = ["Hermionie","Harry","Ron","Draco"]
#houses = ["Gryffindor", "Gryffindor", "Gryffindor", "slytherin"]

#Así se hace un dccionario:
students = {"Hermione": "Gryffindor", 
            "Harry": "Gryffindor",
            "Ron": "Gryffindor",
            "Draco": "Slytherin"
            }                           #Observamos que en cada palabra, le asociamos una definición con ":".
# CASAS DE HOGWARTS
#
# +------------+------------+------------+------------+
# | Hermione   | Harry      | Ron        | Draco      |
# +------------+------------+------------+------------+
# | Gryffindor | Gryffindor | Gryffindor | Slytherin  |
# +------------+------------+------------+------------+
#Para imprimir que cada le corresponde a cada nombre, los diccionarios nos permiten escribir palabras y no posiciones como en
#las listas, ejemplo:
def main1():
    global students
    print(students["Hermione"])
    print(students["Harry"])
    print(students["Ron"])
main1()
#es importante mencionar que lod valores que se definen (los que estan en la izquierda) se llaman keys
#las definiciones se llaman values y finalmente la combinacion de ambos se llaman items.
def main2():
    global students
    for student in students:
        print(student)
main2()
#uno pensaría que el for itera las casas (values), pero solo itera las keys (nombres)
#entonces para ello se hace esto:
def main3():
    global students
    for student in students:
        print(student, students[student])
main3()
#En este programa student itera a students, un diciconario, pero cuando colocamos students[student]
#el programa entiende que quieres imprimir los values también, pueso que student solo son keys
#entonces con [] se trata de los values.
