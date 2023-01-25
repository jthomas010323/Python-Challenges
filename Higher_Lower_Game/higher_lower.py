from art import logo, vs
from info import data
import random
import os
def choose_celeb(data):
    celeb = random.choice(data)
    data.remove(celeb)
    return celeb
score=0
game_over=False
most_followers=""
a=choose_celeb(data)
while not game_over:
    print(logo)
    b=choose_celeb(data)
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
    print(vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
    choice=str(input("Who has more followers? type \"A\" or \"B\": ").lower())
    if a['follower_count']>b['follower_count']:
        most_followers="a"
    else:
        most_followers="b"
    if choice==most_followers:
        score+=1
        a=b
    else:
        game_over=True
    os.system('cls')
    
print(f"Sorry, that's wrong. Final Score: {score}")
    