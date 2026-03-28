'''
Create a Number Guessing Game where:
● The program generates a random number between 1 and 50 using random.
● The user has 5 attempts to guess the number.
● After each guess, calculate the absolute difference using math.fabs() and
display how far the guess is from the correct number.
'''

import random as r
import math as m

Num=r.randint(1,50)
attempts=5
print("Welcome to the Number Guessing Game !")
print("You have 5 attempts to guess the number between 1 & 50!")

for i in range(1,attempts+1):
    guess=int(input(f"Attempt {i}: Guess the number:"))
    if guess>=1 and guess<=50:
       if guess==Num:
         print("You have guessed the correct number!")
         break
       else:
         diff=m.fabs(Num-guess)
         print(f"The guess is {diff} units away from the correct number")
    else:
        print("Error! Enter a number between 1 and 50")
        
if guess!=Num:
    print(f"Game over!, the correct number was {Num}")