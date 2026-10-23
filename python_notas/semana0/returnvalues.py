#ask user for x
x = input ("What´s x:?")
#ask usr for y
y= input ("What´s y?:")
#define z:
z= x + y
#print z
print(f"x + y is equal to: {z}", end="\n\n")
#este codigo concatena, no suma, porque x y y son str no int, usamos funcion int para convertir a int
#entonces lo correcto seria:
z= int(x) + int(y)
print (f"z equals to: {z}")
#otra forma de hacerlo ahorrando lineas pues no necesitas z: IMPORTANTE
x = int(input("what´s x?:"))
y = int(input("What´s y?:"))
#tambien podemos usar fsrt
print(f"x + y equals to: {x+y}")
#tambien puedes vovlerte loco y hacer esto, que no es muy limpio:
print(int(input("What´s x:?"))+int(input("What´s y:?")))
#tambien puedes usar decimales (float
x = float(input("what´s x?:"))
y = float(input("What´s y?:"))

z = round(x / y, 2)#round (redondear, redonde al siguente entero, pero podemos redodnear solo decicameles)
#ejemplo 2/3=0.6666 hara 1 si no pongo ,2 pero si pongo, 2 sera 1
print (z)
#RECUERDA una fstr es simplemente una cadena que permite poner variables en cadenas de texto y ya xd
#Por eso tambien puedes hacer esto, que se ve raro, pero recuerda raro no es difciil:
print(f"{z:.2f}")#solo coloca dos decimale, por defecto al mostrar solo dos, redondea