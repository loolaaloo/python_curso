def main():
    x = int(input("What´s x?: "))
    y = int(input("What´s y?: "))
    if x < y:
        print("X is less than y")
    if x > y:
        print("Y is less than x")
    if x == y:
        print("x is equal to y")
#notemos que usando ifs, se vuelve un camino de 3 preguntas, y tienes que obligatoriamente pasar por todas

#ahora usemos elif
def main1():
    x= int(input("what´s x?:"))
    y= int(input("what´s y?:"))
    if x < y:
        print("x is less than y")
    elif x> y:
        print("x is more than y")
    elif x == y:
        print("x is equal to y")
#en este caso al ser el primer if "false" entonces ejecuta el siguente elif (salta el bloque de if), ahora si este es
#verdadero, entonces ejecuta el bloque y salta al final (ignora los demas elif...)

#Ahora usando ELSE:
def main2():
    x = int(input("what´s x?:"))
    y = int(input("what´s y?:"))
    if x>y:
        print("x is more than y")
    elif x<y:
        print("x is less than y")
    else:
        print("x equals to y")

#main2()
#aca de igual manera ejecuta el if, al ser falso se salta a elfis, al ser falso se va a else, ejecta y va a fin, esto asegura un final
#lo pruebas sin el else, y al ser iguales el programa no acaba y ejecuta linea en blanco
def main3():
    x = int(input("what´s x?:"))
    y = int(input("what´s y?:"))
    if x<y or x>y:
        print("x is not equal to y")
    else:
        print("x is equal to y")