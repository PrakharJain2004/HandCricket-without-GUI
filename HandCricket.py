import random
def bat(comp_runs=10000):
    global user_runs
    user_runs = 0
    while (user_runs<comp_runs):
        user_input= int(input("Type number of runs from 1-6->"))
        if user_input in range(1,7):
            computer_pick = random.randint(1,6)
            print("computer picked ", computer_pick)
            if user_input != computer_pick :
                user_runs += user_input
                print("score: ", user_runs)
            else:
                print('You are OUT\nand your final Score is ',user_runs)
                break
        else:
            print('Invalid Input')
            continue

def bowl(user_runs=10000):
    global comp_runs
    comp_runs = 0
    while (comp_runs<=user_runs):
        user_input= int(input("Type number of runs from 1-6->"))
        if user_input in range(1,7):
            computer_pick = random.randint(1,6)
            print("computer picked ", computer_pick)
            if user_input != computer_pick :
                comp_runs += computer_pick
                print("score: ", comp_runs)
            else:
                print('Computer is OUT\nand the final Score is ',comp_runs)
                break
        else:
            print('Invalid Input')
            continue

comop=['bat','bowl']
#random_number = random.randint(1,6)
while True:
    toss = input("Toss: odd or even? ").lower()
    if toss=="even":
        intoss = int(input("enter your number for the Toss->"))
        if intoss<0:
            print("Input should be Positive \n")
            continue
        else:
            computer_pick = random.randint(1,6)
            sum = computer_pick + intoss
            if sum%2 == 0 :
                tosschoose = input("you won the toss! type 'bat' to bat or 'bowl' to bowl->").lower()
                if tosschoose == "bat":
                    bat()
                    print('Your Batting is Done. Now the computer will bat')
                    bowl(user_runs)
                    if (comp_runs>user_runs):
                        print('You Lost')
                    elif (comp_runs<user_runs):
                        print('You Won')
                    else:
                        print('The game Tied')
                elif tosschoose == "bowl":
                    bowl()
                    print('Computer\'s Batting is Done. Now you will bat')
                    bat(comp_runs)
                    if (comp_runs>user_runs):
                        print('You Lost')
                    elif (comp_runs<user_runs):
                        print('You Won')
                    else:
                        print('The game Tied')
            else:
                randcomop = random.randint(0,1)
                comp_choice= comop[randcomop]
                print("Computer won the toss, and chooses to ", comp_choice)
                if comp_choice == "bowl":
                    bat()
                    print('Your Batting is Done. Now the computer will bat')
                    bowl(user_runs)
                    if (comp_runs>user_runs):
                        print('You Lost')
                    elif (comp_runs<user_runs):
                        print('You Won')
                    else:
                        print('The game Tied')
                elif comp_choice == "bat":
                    bowl()
                    print('Computer\'s Batting is Done. Now you will bat')
                    bat(comp_runs)
                    if (comp_runs>user_runs):
                        print('You Lost')
                    elif (comp_runs<user_runs):
                        print('You Won')
                    else:
                        print('The game Tied')
    elif toss=='odd':
        intoss = int(input("enter your number for the Toss->"))
        if intoss<0:
            print("Input should be Positve \n")
            continue
        else:
            computer_pick = random.randint(1,6)
            sum = computer_pick + intoss
            if sum%2 != 0 :
                tosschoose = input("you won the toss! type 'bat' to bat or 'bowl' to bowl->").lower()
                if tosschoose == "bat":
                    bat()
                    print('Your Batting is Done. Now the computer will bat')
                    bowl(user_runs)
                    if (comp_runs>user_runs):
                        print('You Lost')
                    elif (comp_runs<user_runs):
                        print('You Won')
                    else:
                        print('The game Tied')
                elif tosschoose == "bowl":
                    bowl()
                    print('Computer\'s Batting is Done. Now you will bat')
                    bat(comp_runs)
                    if (comp_runs>user_runs):
                        print('You Lost')
                    elif (comp_runs<user_runs):
                        print('You Won')
                    else:
                        print('The game Tied')
            else:
                randcomop = random.randint(0,1)
                comp_choice= comop[randcomop]
                print("Computer won the toss, and chooses to ", comp_choice)
                if comp_choice == "bowl":
                    bat()
                    print('Your Batting is Done. Now the computer will bat')
                    bowl(user_runs)
                    if (comp_runs>user_runs):
                        print('You Lost')
                    elif (comp_runs<user_runs):
                        print('You Won')
                    else:
                        print('The game Tied')
                elif comp_choice == "bat":
                    bowl()
                    print('Computer\'s Batting is Done. Now you will bat')
                    bat(comp_runs)
                    if (comp_runs>user_runs):
                        print('You Lost')
                    elif (comp_runs<user_runs):
                        print('You Won')
                    else:
                        print('The game Tied')
    else:
        print('Invalid Input')
    con=input('Do you want to continue? (Y/N)->').lower()
    if(con=='y'):
        continue
    else:
        break
