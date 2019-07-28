# SNAKE WATER GUN GAME
import random
list=[1,2,3]
a=random.choice(list)
def game():
    while(True):
            c=int(input("Enter 1 to choose Snake\n"
                        "2 for Gun\n"
                        "3 for Water"))
            if c==1:
                print("Your choice is Snake")
                if a == 1:
                    print(" Computer's choice is Snake")
                    print("Match is tie")
                elif a == 2:
                    print("Computer's choice is Water")
                    print("You won")

                else:
                    print("Computer's choice is Gun")
                    print("You lost")
            elif c==2:
                print("Your choice is Gun")
                if a == 1:
                    print(" Computer's choice is Snake")
                    print("You won")
                elif a == 2:
                    print("Computer's choice is Water")
                    print("You lost")
                else:
                    print("Computer's choice is Gun")
                    print("Match is tie")
            elif c==3:
                print("Your choice is Water")
                if a == 1:
                    print(" Computer's choice is Snake")
                    print("You lost")
                elif a == 2:
                    print("Computer's choice is Water")
                    print("Match is tie")
                else:
                    print("Computer's choice is Gun")
                    print("You won")
            d=input("Enter Y if you want to play further\n"
                        "Enter N if you don't want to continue")
            e=d.lower()
            if e=="n":
                break
    print("See you again!!")

print("{0:*^120}".format("SNAKE WATER GUN GAME"))
b=int(input("If you know the rules then enter 1 To play  else enter 2 TO know the Rules"))
if b==1:
    print("{0:*^120}".format("Welcome to the game"))
    game()
if b==2:
    print("The Rules for the game are:\n"
          "Between Snake and water : Snake wins\n"
          "Between Snake and Gun:Gun wins\n"
          "Between Water and Gun:Water wins\n")
    game()
