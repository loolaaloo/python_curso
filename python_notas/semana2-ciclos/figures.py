#-------------------Ciclos anidados--------------

def main1():
    print_square(3)

def print_square(size):
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
                    
main1()
#Se trata de un for que imprime 3 veces "#", al cumplirse esto el primero for i in range(size):, repite otra vez
#lo que tiene en su bloque identado, pero antes se imprime el enter, justo cuando acaba el for j in range(size):
#imprime el enter. Detalle importante print() y print(""), hacen lo mismo.

#----------------También podemos hacer esto:--------------
def main4():
    def main3():
        print_square(6)
    def print_square(size):
         for i in range(size):
              print("#" *6, end="")
              print()
    main3()
main4()
#También lo podemos hacer así:

def main5():
    def main6():
          print_square(9)
    def print_square(size):
         for i in range(size):
              print_row(size)
    def print_row(width):
         print("#" * width)
    main6()
main5()