import random
import os
from hangman_art import logo, stages
from hangman_words import word_list
print(logo)
clear = lambda: os.system('cls')
used_words=[]
game_over= False
underline_list=[]
random_word_list=[]
lives=6
random_word=random.choice(word_list)
for i in range(0, len(random_word)):
    random_word_list.append(random_word[i])
    underline_list.append('_')
    
while game_over==False and lives>0:
  guess=input("Choose a letter: ").lower()
  clear()
  if random_word.count(guess):
    for i in range(len(random_word)):
      if guess==random_word[i]:
        underline_list[i] = guess
  else:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives-=1
    used_words.append(guess)
 
  print(stages[lives])
  print(underline_list)
  print(used_words)
  if underline_list==random_word_list:
    game_over= True
    print("You win!") 
  elif lives==0:
    print(f"You ran out of lives. You lose. The word was {random_word}")
  