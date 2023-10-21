#### THIS GAME IS CREATED BY OZ-CODEZ ########

print("Welcome to the Hangman")

word_list = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
import random

chosen_word = random.choice(word_list)

guessed_word = []
for letter in chosen_word:
    guessed_word.append("_")

live = 6

print(HANGMANPICS[0])

hang_counter = 1

while "_" in guessed_word and not live == 0 :
    guess = input("Guess a letter: ").lower()
    if(guess in guessed_word):
        print(f"You`ve already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            guessed_word[position] = letter
    print(guessed_word)
    if guess not in chosen_word:
        print(HANGMANPICS[hang_counter])
        hang_counter+=1
        live -= 1


if(live ==0):
    print("You lose")
else:
    print("You win the word was ")
    print(*chosen_word, sep="")
