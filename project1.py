import random
computer=random.choice(["Rock","Paper","Scissor"])
ystr=input("Enter your choice:")



print(f"You chose:\t{ystr}\nComputer chose:\t{computer}")
if(computer==ystr):
    print("Its a draw")
else:

    if(ystr=="Rock" and computer=="Paper"):
        print("you won")
    elif(ystr=="Rock" and computer=="Scissor"):
        print("you loose")
    elif(ystr== "Paper" and computer=="Rock"):
        print("you loose")
    elif(ystr=="Paper" and computer=="Scissor"):
        print("you won")
    elif(ystr=="Scissor" and computer=="Rock"):
        print("you loose")
    elif(ystr=="Scissor" and computer=="Paper"):
        print("you won")