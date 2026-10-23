#SCOOPE SE TRATA DE CUANDO DEFINES UNA FUNCION QUE SOLO EXISTE EN EL CONTEXTO EN EL QUE LA DEFINISTE
#ES DECIR ENTRE CAJITAS (FUINCIONES CREADAS) NO EXISTEN LAS MISMAS VARIABLES:
def main():
    name=input("What´s your name?: ")
    hello() #llamas a otra funcion

def hello():
    print("hello", name) #notese como llamas a una variable que se definio en main
#para resolver esto estan pues los parametros que interconectan :D
main()
def main1():
    name=input("What´s your name?: ")
    hello1(name)

def hello1(to): #definimos parametro para interconectar  
    print("hello", to)
main1() #:D
#A LO ANTERIOR SE LE LLAMA SCOOPE
#esto sed debe a que asi es por defecto el programa python, entonces no es como en ensamblador que
#se quedaba "a la mano" porque es una memoria fisica
#cada que defines una funcion se crea una cajita que hace invisible a todas las demas cajas
#lo que tiene esta adentro