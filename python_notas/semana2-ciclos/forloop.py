#--------------- For loop (short) -----------------
def main1():
    def main():
        names = ["mario", "Luigi", "Daysi", "Yoshi"]
        for name in names:
            print(write_letter(name))


    def write_letter(name):
        return f"""
        -------------------------------------------
        Dear {name}, you are cordially invited to
        a ball at Peach´s Castle at 7:00 PM.
        Sincerly
        Princess Peach
        -------------------------------------------
        """
    main()
#main1()

#Otra manera:
#Recuerda que cuando escribes lista[number], escribes la posicion, es decir si coloco
#name[1], va a impirmir Luigi
def main2():
    def main():
        names=["Mario", "Luigi", "Daysi", "Yoshi"]
        for i in range(len(names)):
            print(write_letter(names[i])) #Aqui al colocar names[i], va recorriendo cada elemento de la lista.
    def write_letter(name):
        return f"""
        -------------------------------------------
        Dear {name}, you are cordially invited to
        a ball at Peach´s Castle at 7:00 PM.
        Sincerly
        Princess Peach
        -------------------------------------------
        """
    main()
#main2()

#------------ Lists -------------------
#aca usarmeos .append() sirve para agregar un unico elemento a una lista
#la ventaja es que acepta cualquier tipo de dato, numeros, cadenas, objetos incluso otra lista...
def main3():
    lista = ["luigi", "mario"]
    lista.append("Peach")
    lista.append("Bowser")
    lista.append("Koopa Troopa")

    lista.append(["Bowser", "Donkey"])
    lista.remove(["Bowser", "Donkey"])
    lista.extend(["Bowser", "Donkey"])
    print(lista)
main3()
#Tambien se usa .remove() que por evidente que es, quita elementos de una lista
#Como .append solo agrega uno y solo un dato, usamos extend
#La diferencia entre ambos se describe a continuación:
def main4():
    a = [1,2]
    b = [3,4,5]
    a.extend(b)
#lo que hace es esto, añade elemento por elemento, uno a uno
#Toma el 1er elemento de b → 3 → lo agrega a a  → [1, 2, 3]
#Toma el 2do elemento de b → 4 → lo agrega a a  → [1, 2, 3, 4]
#Toma el 3er elemento de b → 5 → lo agrega a a  → [1, 2, 3, 4, 5]   
    a.append(b)
#lo que hace es agregar todos los elementos en un solo movimiento:
# Resultado: [1, 2, [3, 4, 5]]
#Con cadenas .extend() tambien itera
    c = ["x","y"]
    c.extend("ab")
#Resultado: ['x', 'y', 'a', 'b']
#IMPORTANTE:
#OBSERVESE QUE: es diferente colocar .extend("something") a .extend(["something"])
#en el primero agregara letra a letra y en el segundo al ser una lista, la agrega completa
#puesto que python piensa que solo es un caracter o elemento, como quieras llamarl.

#Ahora le daremos uso a .insert(), que inserta como es claro, un nuevo elemento en una lista
#solo que te da la versatilidad de agregarlo en la posicion que desees
#respetando que 0 es el primer elemento de la lista, 1 el segundo y asi sucesivamente.
def main5():
    