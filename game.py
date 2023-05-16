"""A number-guessing game."""
import random
from random import randint
# Put your code here
print("Welcome to game")
name = input ("what's your name ? :")
secret_number = random.randint(1, 10)
# print(secret_number)
print(name, 'I am thinking of a number between 1 and 100')
compt = 0
while (True):
    guess = int(input("Your guess ? : "))
    compt += 1
    if int(guess) == False:
        print(name, 'Your guess is not an integer, try again')
    elif(guess < 0 or guess > 100):
        print(name, 'Your guess is not between 1 and 100, try again')  
    elif( guess < secret_number ):
        print(name, 'Your guess is too low, try again')
    elif ( guess > secret_number):
        print(name, 'Your guess is too hight, try again')
    elif (guess == secret_number) : 
        print('Well done', name, '! You found my number in', compt, ' tries! ')
        break
    