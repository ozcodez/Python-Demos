import random

def create_number():
    num = random.randint(1,100)
    return num

def choose_difficult(param1):
    if(param1 == "easy"):
        return 10
    else:
        return 5

def guessing(guess,answer):
    if(guess<answer):
        print("too low")
    elif(guess>answer):
        print("too high")

def play_game():
    number = create_number()
    difficult = input("Choose difficult easy or hard")
    lives = choose_difficult(difficult)
    print(f"You have {lives} lives")
    guess =-5
    while(lives>0 and guess !=number ):
        guess = int(input("Guess the number"))
        guessing(guess,number)
        lives -=1
        print(f"You have {lives} lives left")

    if(lives == 0):
        print(f"you lose the number was {number}")
    else:
        print(f"you win with {lives} lives left. The number was {number}")


do_u_want_cont = True

while(do_u_want_cont):
    play_game()
    ask = input("Do you want to continue y or n")
    if(ask=="n"):
        do_u_want_cont=False

print("Goodbye")