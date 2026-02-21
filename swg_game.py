import random
'''
1 for snake
-1 for water
0 for gun

'''

computer = random.choice([1,-1,0])
youstr = (input("Enter your choice: "))
yourDict= {"s": 1,"w": -1,"g": 0}
reverseDict= {1: "snake", -1: "water",0: "gun"}

you=yourDict[youstr]
#By now here we have two numbers i.e you and computer

print(f"you chose {reverseDict[you]}\n computer chose {reverseDict[computer]}")

if(computer==you):
    print("It's a draw")
    
else:
    if(computer==1 and you==-1):
        print("you lose!")
    elif(computer==1 and you==0):
        print("you won!")
    elif(computer==-1 and you==1):
        print("you won!")
    elif(computer==-1 and you==0):
        print("you lose!")
    elif(computer==0 and you==-1):
        print("you won!")
    elif(computer==0 and you==1):
        print("you lose!")
    else:
        print("something went wrong")