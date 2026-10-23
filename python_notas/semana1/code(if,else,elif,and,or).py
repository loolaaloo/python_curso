def main():
    score=int(input("Score: "))
    if score >= 90:
        print("Score: A")
    elif score>= 80:
        print("Score: V")
    elif score >= 70:
        print("Score: D")
    elif score >= 60:
        print("Score: D")
    else:
        print ("Score: F")
#main()
#Explanation: In this case the first if (false)  then the program jumps to elif (false)
#then jumps to the next elif (true), remember, when an elif is (true), executes the code on the indantation
#then jumps to the end of the function
#elif ignores the others elifs and the first if is (false) so the code indantation is ignored

#let´s create a more difficult program, that ask the user betwen two difficulties (Casual or Difficult) and between (Sigle-player or Multiplayer)

def main1():
    difficulty = input("Difficult or Casual?: ")
    players = input("Single-player or Multiplayer?: ")

    if difficulty == "Difficult":
        if players == "Single-player":
            recommend("Cuphead")
        elif players == "Multiplayer":
            recommend("Fornite")
        else:
            print("Choose a valid players...")
    elif difficulty == "Casual":
        if players == "Single-player":
            recommend("Minecraft")
        elif players == "Multiplayer":
            recommend("Call of duty")
        else:
            print("Choose a valid players...")
    else:
        print("Choose a valid difficulty...")

def recommend(game):
    print(f"You migth like: {game}")

main1()
#the progrmam could´nt run if the user dont use the capital letters or if theres some space at the end 
#easy to solve this problem if you use this at the end .lower(), pone en minuscular todo
#and for the extra spaces .strip(), en los parentesis borras lo que no quieres al final, en este caso espacio