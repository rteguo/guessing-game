"""A number-guessing game."""
import random
from random import randint
# Put your code here
print("Welcome to game")
name = input ("what's your name ? :")
secret_number = random.randint(1, 10)
print(secret_number)
print(name, 'I am thinking of a number between 1 and 100')
too_low = 0
too_hight = 101
compt = 1
while (1 == 1):
    guess = int(input("Your guess ? : "))
    #guess = int ((too_low + too_hight) / 2)
    if( guess < secret_number ):
        print(name, 'Your guess is too low, try again')
        too_hight = secret_number
    else:
        if ( guess > secret_number):
            print(name, 'Your guess is too hight, try again')
            too_low = secret_number
    if (guess == secret_number) : 
        print('Well done', name, '! You found my number in', compt, ' tries! ')
        break
    compt += 1