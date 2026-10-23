#calculadora sencilla
#def main():
  #  x=input("What´s x?: ")
 #   print(f"square x is: {square(x)}")

#def square(n):
   # return x*x
#main()
#ahora usemos return para una calculadora de area:
#def main():
 #   house = area(50 ,29)
  #  yard = area(20,1)
   # print(str(house + yard) + "square feet")
#def area(long,width):
 #   print(str(width*long)+ " square feet")
  #  return width*long
    
#main()
#primero el programa lee que solo llamas main, luego en main house esta definiciod por la funcion 
#area con los parametros 50 y 20, entonces va a area funcion y los multiplica
#luego impirme lo que vale el area de casa y con return regresa a house el valor a la derecha de return
#luego lo mismo para yard pero con otros valores :v
#def main():
 #   long = int(input("what´s the long?: "))
  #  width= int(input("whats the width?: "))
   # area(long,width)

#def area(l,w):
 #   print("the area is: " + str(l*w))
  #  return l*w
#main()

def main():
   long1 = int(input("whats the long1?: "))
   width1 = int(input("what´s the widthd1: "))
   house = area(long1, width1)
   long2 = int(input("whats the long2?: "))
   width2 = int(input("what´s the widthd2: "))
   yard = area(long2,width2)
   print("the total area is: ", str(house+yard))
def area(l,w):
    print("the area is :", str(l*w))
    return l*w
main()
