"""
-> This is an example program
-> Made by smokeynoom
"""

# Maths Game
import pbasic as b
import random as r

print("Welcome to Basic Math. Answer all the questions.")
name = input("Please enter your name: ")
print(f"Ok {name}, let's start.")

num1 = r.randrange(0, 100)
num2 = r.randrange(0, 100)
correct_answer = num1 + num2

user_answer = input(f"What is {num1} + {num2}: ")
print(f"The correct answer is {correct_answer}")

if str(correct_answer) == str(user_answer):
    print("Your answer is Correct! ✅")

else: 
    print("Your answer is Wrong! ❌")
