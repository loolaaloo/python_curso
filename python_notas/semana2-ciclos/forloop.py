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
main2()