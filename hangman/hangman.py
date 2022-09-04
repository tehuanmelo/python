# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    hangman.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tehuanmelo <tehuanmelo@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/04 23:33:12 by tehuanmelo        #+#    #+#              #
#    Updated: 2022/09/04 23:35:19 by tehuanmelo       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import random
import os
from hangman_art import logo, stages, prize
from hangman_words import word_list
os.system('clear')

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
display = []
guessed = []

print(logo)

for _ in range(word_length):
    display += "_"

while not end_of_game:

    # print(f'Pssst, the solution is {chosen_word}.')
    guess = input("Guess a letter: ").lower()
    os.system('clear')
    
    print(logo)

    if guess in guessed:
      print("You already entered this letter")
    elif guess not in chosen_word:
        guessed += guess
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    else:
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
              guessed += letter 
 
    if "_" not in display:
        end_of_game = True
        print("You win")
    
    
    print(f"{' '.join(display)}")
    print(stages[lives])
    