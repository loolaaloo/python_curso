#quiero hacer una funcion que cada que le hago llamada (call), haga lo que le dije, para eso son
#ejemplo, quiero una funcion que cada que la uso, me imprima hello
def hellofunc():
    print("hello")

hellofunc()
#pero podemos hacerlo mejor, usando parametros de la funcion que acabamos de crear:
def hello(to,age):
    print("hello", to, age)

name=input("what´s ypur name?: ")
anciano=input("what´s ypur age?: ")

hello (name,anciano)
#entonces va a "equivaler" los valores ingresados con el  usuario en el vector de hello, es ir y volver
#pero sirve par entender el concepto por ahora 
#tambien podemos definir dentro de nuestra funcion definida el valor de los parametros en el vector
def hello2(to="world"):
    print("Hello", to)
hello2() #por defecto to=wordl impimira hello world perio despues to puede cambiar
name=input("What´s your name?: ")
hello2(name)#pidio nombre ahora imprime hello luis por decir
