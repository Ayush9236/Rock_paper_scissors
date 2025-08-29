import random
computer=random.choice([-1,0,1])
print("Enter r for Rock")
print("Enter s for Scissor")
print("Enter p for Paper")
ystr=input("Enter your choice:")
ydict={"r":1,"p":-1,"s":0}
reversedict={1:"Rock",-1:"Paper",0:"Scissor"}
you=ydict[ystr]
print(f"You chose:\t{reversedict[you]}\nComputer chose:\t{reversedict[computer]}")
if(computer==you):
    print("Its a draw")
else:
    if(you==-1 and computer==1):
        print("you won")
    elif(you==-1 and computer==0):
        print("you loose")
    elif(you==1 and computer==-1):
        print("you loose")
    elif(you==1 and computer==0):
        print("you won")
    elif(you==0 and computer==-1):
        print("you won")
    elif(you==0 and computer==1):
        print("you loose")
    else:
        print("SOS")
        