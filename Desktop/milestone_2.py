import random 

#List of my 5 favourite fruits
word_list = ["Apple", "Blueberry", "Banana", "Orange", "Melon"]

#Random selection of my fruits
word = random.choice(word_list)

#Input a letter to guess the fruits
guess = input('input a letter: ')

if len(guess) == 1 and guess.isalpha():
     print('good guess!')
else: print('Oops, That is not a valid input')
