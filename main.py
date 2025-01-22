#!/opt/anaconda3/bin/python


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
