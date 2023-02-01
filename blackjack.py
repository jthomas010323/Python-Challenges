import random
import os
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
p_deck=[]
cp_deck=[]

def draw_card(deck, cards):
    deck.append(random.choice(cards))

def calculate_score(deck):
    score=0
    ace=False
    ace_index=0
    for i in range(len(deck)):
        if deck[i]==11:
            ace=True
            ace_index=i
        score+=deck[i]
    if score>21 and ace:
        deck[ace_index]=1
        score=score-10
    return score    
        
game_over=False
game_continue=str(input("Do you want to play blackjack (y or n): ")).lower()
while game_continue=='y':
    os.system('cls')
    
    draw_card(p_deck, cards)
    draw_card(p_deck, cards)
    p_score=calculate_score(p_deck)
    print("Your cards: "+ str(p_deck) +", current score: " + str(p_score) )
    draw_card(cp_deck, cards)
    draw_card(cp_deck, cards)
    cp_score = calculate_score(cp_deck)
    print("Computers first card: " + str(cp_deck[0]))
    another_card=input("Type d to get another card or s to stand: " ).lower()
    while another_card=="d":
        draw_card(p_deck, cards)
        p_score=calculate_score(p_deck)
        print("Your cards: "+ str(p_deck) +", current score: " + str(p_score) )
        print("Computers first card: " + str(cp_deck[0]))
        if p_score>21:
            print("Your final hand: "+ str(p_deck) +", current score: " + str(p_score))
            print("Computer's final hand: "+ str(cp_deck) +", current score: " + str(cp_score) )
            print("You went over, You lose :(")
            game_over=True
            break
        another_card=input("Type d to get another card or N to stand: " ).lower()
    if not game_over:
        while cp_score<17:
            draw_card(cp_deck, cards)
            cp_score = calculate_score(cp_deck)
        print("Your final hand: "+ str(p_deck) +", current score: " + str(p_score))
        print("Computer's final hand: "+ str(cp_deck) +", current score: " + str(cp_score) )
        if cp_score>21:
            print("You won!")
        elif cp_score<p_score:
            print("You win")
        elif cp_score>p_score:
            print("You lose,,,")
        elif cp_score==p_score:
            print("Draw")
    p_deck=[]
    cp_deck=[]
    game_continue=str(input("Do you want to play blackjack (y or n): ")).lower()
    
    