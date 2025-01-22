#!/opt/anaconda3/bin/python

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")
firstI = input("You're at a crossroad. Where do you want to go?\n     Type 'left' or 'right'\n")
if firstI == 'right':
    print("Game Over")
else:
    print("You've come to a lake. There is an island in the middle of the lake.")
    secondI = input('Type "wait" to wait for a boat. Type "swim" to swim across.\n')
    if secondI == 'swim':
        print("Game Over")
    else:
        print("You arrive at the island unharmed. There is a houe with 3 doors. One red, one yellow and one blue.")
        thirdI = input("Which colour do you choose?")
        if thirdI == 'red' or thirdI == 'blue':
            print("Game Over")
        elif thirdI == 'yellow':
            print("You win!")
        else:
            print("Game over")
