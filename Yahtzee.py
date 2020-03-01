#Yahtzee

one = """
 __________
|          |
|          |
|     @    |
|          |
|__________|
"""

two = """
 __________
|          |
|       @  |
|          |
|  @       |
|__________|
"""

three = """
 __________
|          |
|        @ |
|     @    |
|  @       |
|__________|
"""

four = """
 __________
|          |
|  @    @  |
|          |
|  @    @  |
|__________|
"""

five = """
 __________
|          |
|  @    @  |
|     @    |
|  @    @  |
|__________|
"""

six = """
 __________
|          |
|  @  @  @ |
|          |
|  @  @  @ |
|__________|
"""

import random

def fourOfAKind(dielist):
    argument = hasAtLeastN(dielist, 4)
    if argument == 1:
        total = sumDice(dielist)
        return total
    else:
        return 0

def fullHouse(dielist):
    argument2 = hasExactlyN(dielist, 2)
    argument3 = hasExactlyN(dielist, 3)
    argument5 = hasExactlyN(dielist, 5)
    if argument2 == 1 and argument3 == 1:
        return 25
    elif argument5 == 1:
        return 25
    else:
        return 0

def hasAtLeastN(dielist, n):
    f1 = dielist.count(1)
    f2 = dielist.count(2)
    f3 = dielist.count(3)
    f4 = dielist.count(4)
    f5 = dielist.count(5)
    f6 = dielist.count(6)
    if f1 >= n or f2 >= n or f3 >= n or f4 >= n or f5 >= n or f6 >= n:
        return 1
    else:
        return 0

def hasExactlyN(dielist, n):
    f1 = dielist.count(1)
    f2 = dielist.count(2)
    f3 = dielist.count(3)
    f4 = dielist.count(4)
    f5 = dielist.count(5)
    f6 = dielist.count(6)
    if f1 == n or f2 == n or f3 == n or f4 == n or f5 == n or f6 == n:
        return 1
    else:
        return 0

def largeStraight(dielist):
    combos = ([1,2,3,4,5], [2,3,4,5,6])
    dielist.sort()
    if dielist in combos:
        return 40
    else:
        return 0

def realscores():
    print("Ones:", ones_score)
    print("Twos:", twos_score)
    print("Threes:", threes_score)
    print("Fours:", fours_score)
    print("Fives:", fives_score)
    print("Sixes:", sixes_score)
    print("Three Of A Kind:", ofAKind3_score)
    print("Four Of A Kind:", ofAKind4_score)
    print("Full House:", fhouse_score)
    print("Small Straight:", smstrt_score)
    print("Large Straight:", lgstrt_score)
    print("Yahtzee:", yahtzee_score)
    print("Chance:", chance_score)
    
def reroll(choices):
    print(choices)
    if "A" in choices:
        del dielist[0]
        dielist.insert(0, random.randint(1,6))
    if "B" in choices:
        del dielist[1]
        dielist.insert(1, random.randint(1,6))
    if "C" in choices:
        del dielist[2]
        dielist.insert(2, random.randint(1,6))
    if "D" in choices:
        del dielist[3]
        dielist.insert(3, random.randint(1,6))
    if "E" in choices:
        del dielist[4]
        dielist.insert(4, random.randint(1,6))
    if choices == "":
        return 1
    elif "A" not in choices and "B" not in choices and "C" not in choices and "D" not in choices and "E" not in choices:
        return 0
    
def roll():
    x = 0
    while x < 5:
        die = random.randint(1,6)
        dielist.append(die)
        x += 1
    return dielist

def showdice(dielist):
    print(dielist)

def showscores(dielist):
    print("1. Ones:\t\t", sumOfN(dielist, 1))
    print("2. Twos:\t\t", sumOfN(dielist, 2))
    print("3. Threes:\t\t", sumOfN(dielist, 3))
    print("4. Fours:\t\t", sumOfN(dielist, 4))
    print("5. Fives:\t\t", sumOfN(dielist, 5))
    print("6. Sixes:\t\t", sumOfN(dielist, 6))
    print("7. Three Of A Kind:\t", threeOfAKind(dielist))
    print("8. Four Of A Kind:\t", fourOfAKind(dielist))
    print("9. Full House:\t\t", fullHouse(dielist))
    print("10. Small Straight:\t", smallStraight(dielist))
    print("11. Large Straight:\t", largeStraight(dielist))
    print("12. Yahtzee:\t\t", yahtzee(dielist))
    print("13. Chance:\t\t", sumDice(dielist))

def smallStraight(dielist):
    combos = ([1,1,2,3,4], [1,2,2,3,4], [1,2,3,3,4], [1,2,3,4,4], [1,2,3,4,5], [1,2,3,4,6],
              [2,2,3,4,5], [2,3,3,4,5], [2,3,4,4,5], [2,3,4,5,5], [2,3,4,5,6],
              [1,3,4,5,6], [3,3,4,5,6], [3,4,4,5,6], [3,4,5,5,6], [3,4,5,6,6])
    dielist.sort()
    if dielist in combos:
        return 30
    else:
        return 0    
    
def sumDice(dielist):
    sum_ = 0
    sum_ += sumOfN(dielist, 1)
    sum_ += sumOfN(dielist, 2)
    sum_ += sumOfN(dielist, 3)
    sum_ += sumOfN(dielist, 4)
    sum_ += sumOfN(dielist, 5)
    sum_ += sumOfN(dielist, 6)
    return sum_

def sumOfN(dielist, num):
    sumN = dielist.count(num) * num
    return sumN

def threeOfAKind(dielist):
    argument = hasAtLeastN(dielist, 3)
    if argument == 1:
        total = sumDice(dielist)
        return total
    else:
        return 0

def yahtzee(dielist):
    argument = hasExactlyN(dielist, 5)
    if argument == 1:
        return 50
    else:
        return 0
    
#Every necessary variable/list:
dielist = []
rolls = 0
slots = 0
ones_slot = 0   #These are for if they are used
twos_slot = 0
threes_slot = 0
fours_slot = 0
fives_slot = 0
sixes_slot = 0
ofAKind3_slot = 0
ofAKind4_slot = 0
fhouse_slot = 0
smstrt_slot = 0
lgstrt_slot = 0
yahtzee_slot = 0
chance_slot = 0
ones_score = 0  #These are actual scores
twos_score = 0
threes_score = 0
fours_score = 0
fives_score = 0
sixes_score = 0
ofAKind3_score = 0
ofAKind4_score = 0
fhouse_score = 0
smstrt_score = 0
lgstrt_score = 0
yahtzee_score = 0
chance_score = 0

#intro

print("""
____    ____  ___       __    __  .___________.________   _______  _______ 
\   \  /   / /   \     |  |  |  | |           |       /  |   ____||   ____|
 \   \/   / /  ^  \    |  |__|  | `---|  |----`---/  /   |  |__   |  |__   
  \_    _/ /  /_\  \   |   __   |     |  |       /  /    |   __|  |   __|  
    |  |  /  _____  \  |  |  |  |     |  |      /  /----.|  |____ |  |____ 
    |__| /__/     \__\ |__|  |__|     |__|     /________||_______||_______|
    """)
highscore = 196     #Max Score is 340
print("High Score:", highscore)

#main

while slots < 13:
    dielist = []
    roll()
    while rolls < 2:
        print()
        print("""Position:  A B C D E""")
        print("   Value: ", dielist[0], dielist[1], dielist[2], dielist[3], dielist[4])
        a = reroll(input("Enter dice to re-roll: "))
        if a == 0:
            reroll(input("That is an invalid input, re-enter the dice you want to re-roll: "))
        rolls += 1
    if rolls == 2:
        print("""Position:  A B C D E""")
        print("   Value: ", dielist[0], dielist[1], dielist[2], dielist[3], dielist[4])
        print("Possible Scores for Roll:")
        print("\nSlot\t\t\t Points")
        showscores(dielist)
        z = 0   #For while loop
        while z == 0:
            slotchoice = input("Choose a slot to score (Enter the number): ")
            if slotchoice == "1":
                if ones_slot == 1:
                    print("This slot has already been used.")
                elif ones_slot == 0:
                    ones_slot = 1
                    ones_score = sumOfN(dielist, 1)
                    z = 1
            elif slotchoice == "2":
                if twos_slot == 1:
                    print("This slot has already been used.")
                elif twos_slot == 0:
                    twos_slot = 1
                    twos_score = sumOfN(dielist, 2)
                    z = 1
            elif slotchoice == "3":
                if threes_slot == 1:
                    print("This slot has already been used.")
                elif threes_slot == 0:
                    threes_slot = 1
                    threes_score = sumOfN(dielist, 3)
                    z = 1
            elif slotchoice == "4":
                if fours_slot == 1:
                    print("This slot has already been used.")
                elif fours_slot == 0:
                    fours_slot = 1
                    fours_score = sumOfN(dielist, 4)
                    z = 1
            elif slotchoice == "5":
                if fives_slot == 1:
                    print("This slot has already been used.")
                elif fives_slot == 0:
                    fives_slot = 1
                    fives_score = sumOfN(dielist, 5)
                    z = 1
            elif slotchoice == "6":
                if sixes_slot == 1:
                    print("This slot has already been used.")
                elif sixes_slot == 0:
                    sixes_slot = 1
                    sixes_score = sumOfN(dielist, 6)
                    z = 1
            elif slotchoice == "7":
                if ofAKind3_slot == 1:
                    print("This slot has already been used.")
                elif ofAKind3_slot == 0:
                    ofAKind3_slot = 1
                    ofAKind3_score = threeOfAKind(dielist)
                    z = 1
            elif slotchoice == "8":
                if ofAKind4_slot == 1:
                    print("This slot has already been used.")
                elif ofAKind4_slot == 0:
                    ofAKind4_slot = 1
                    ofAKind4_score = fourOfAKind(dielist)
                    z = 1
            elif slotchoice == "9":
                if fhouse_slot == 1:
                    print("This slot has already been used.")
                elif fhouse_slot == 0:
                    fhouse_slot = 1
                    fhouse_score = fullHouse(dielist)
                    z = 1
            elif slotchoice == "10":
                if smstrt_slot == 1:
                    print("This slot has already been used.")
                elif smstrt_slot == 0:
                    smstrt_slot = 1
                    smstrt_score = smallStraight(dielist)
                    z = 1
            elif slotchoice == "11":
                if lgstrt_slot == 1:
                    print("This slot has already been used.")
                elif lgstrt_slot == 0:
                    lgstrt_slot = 1
                    lgstrt_score = largeStraight(dielist)
                    z = 1
            elif slotchoice == "12":
                if yahtzee_slot == 1:
                    print("This slot has already been used.")
                elif yahtzee_slot == 0:
                    yahtzee_slot = 1
                    yahtzee_score = yahtzee(dielist)
                    z = 1
            elif slotchoice == "13":
                if chance_slot == 1:
                    print("This slot has already been used.")
                elif chance_slot == 0:
                    chance_slot = 1
                    chance_score = sumDice(dielist)
                    z = 1
            else:
                print("Type the number of the slot you want to choose.")
            slotchoice = 0
        slots += 1
        print("\nCurrent Scores:")
        realscores()
        print("Total:", ones_score + twos_score + threes_score + fours_score + fives_score + sixes_score + smstrt_score + lgstrt_score + yahtzee_score + chance_score)
        rolls = 0

#End of Game
print()
print("""
 _____                  _____             
|   __|___ _____ ___   |     |_ _ ___ ___ 
|  |  | .'|     | -_|  |  |  | | | -_|  _|
|_____|__,|_|_|_|___|  |_____|\_/|___|_|
""")
print("\nFinal Scores:")
realscores()
totalscore = ones_score + twos_score + threes_score + fours_score + fives_score + sixes_score + smstrt_score + lgstrt_score + yahtzee_score + chance_score
print("Total:", totalscore)
if totalscore > highscore:
    print("New High Score!")


input("\n\nPress enter to exit.")






