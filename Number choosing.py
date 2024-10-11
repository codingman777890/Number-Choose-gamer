import random
print("Welcome to Number Guessing game")
print("What level you want to play")
print("Easy")
print("Medium")
print("Hard")
print("Impossible")
user = input("Enter your level: ")

if user == "Easy":
    print("You have choose the level Easy")
    number = random.randint(1, 10)
    attempts = 10
    while attempts > 0:
        guess = int(input("Get Ready | Enter the number"))
        if guess == number:
            print("You Won")
            break
        elif guess > number:
            print("little high")
        elif guess < number:
            print("little low")
        if attempts == 0:
            print("You Lose | Try again")
            break
if user == "Medium":
    print("You have choose the level Medium")
    number2 = random.randint(1, 50)
    attempts2 = 5
    while attempts2 > 0:
        guess2 = int(input("Get Ready | Enter the number"))
        if guess2 == number2:
            print("You Won")
            break
        elif guess2 > number2:
            print("little high")
        elif guess2 < number2:
            print("little low")
        if attempts2 == 0:
            print("you lose | Try again")
            break
if user == "Hard":
    print("You choose the level Hard")
    number3 = random.randint(1, 100)
    attempts3 = 2
    while attempts3 > 0:
        guess3 = int(input("Get Ready | Enter the number: "))
        if guess3 == number3:
            print("You Won!")
            break
        elif guess3 > number3:
            print("little high")
        elif guess3 < number3:
            print("little low")
        attempts3 -= 1
        if attempts3 == 0:
            print("You lose | Try again")
            print(f"The number was {number3}")
            break
if user == "Impossible":
    print("You have chosen the level Impossible")
    number4 = random.randint(1, 2000)
    attempts4 = 1
    while attempts4 > 0:
        guess4 = int(input("Get Ready | Enter the number: "))
        if guess4 == number4:
            print("You Won!")
            print("You have unlocked a new level: GOD")
            play_god = input("Do you want to play the GOD level? (Yes/No): ")
            if play_god.lower() == "yes":
                print("YOU ARE IN THE LEVEL GOD. PLAY CAREFULLY!")
                number5 = random.randint(1, 5000)
                attempts5 = 5
                while attempts5 > 0:
                    guess5 = int(input("Get Ready | Enter the number: "))
                    if guess5 == number5:
                        print("You Won!")
                        print("Congratulations, You have won the game")
                        print("You are the GOD of this game")
                        print("Thank you for playing from the Creator of this game")
                        break
                    elif guess5 > number5:
                        print("little high")
                    elif guess5 < number5:
                        print("little low")
                    attempts5 -= 1
                    if attempts5 == 0:
                        print("You lose | The number was", number5)
                break
            else:
                print("Thank you for playing!")
                break
        elif guess4 > number4:
            print("little high")
        elif guess4 < number4:
            print("little low")
        attempts4 -= 1
        if attempts4 == 0:
            print("You lose | The number was", number4)
            #MADE BY RISHABH GHOSH
