import random

import database


def increase_score(score):
    score+=1
    return score

score =0

print("Welcome to higher lower")

game_over =False
while(not game_over):
    compare_a= random.choice(database.data)
    compare_b= random.choice(database.data)
    if(compare_a["follower_count"] > compare_b["follower_count"]):
        answer = "A"
    elif(compare_a["follower_count"] < compare_b["follower_count"]):
        answer = "B"
    else:
        answer = "SAME"

    print(f"First one is {compare_a['name']}, a {compare_a['description']} from {compare_a['country']} ")
    print(f"The other one is {compare_b['name']}, a {compare_b['description']} from {compare_b['country']} ")
    user_answer = input("If you want to first one is higher type A, second one is higher type B, if they are same type SAME")
    if(user_answer==answer):
        print("Correct. Next question is below")
        score = increase_score(score)
    else:
        print(f"Game over your score is {score}")
        game_over = True

