# Imports
import random

# Variables
coinScore = 0

# Functions
def coinflip():
  global coinScore
  while True:
    answer = input("Do you want to flip a coin? (y/n)\n ")
    if answer == "n":
      print(f"Your score was {coinScore}!")
      break
    result = random.randint(1, 2)
    if result == 2:
      coinScore += 1
    print(f"Your score was {coinScore}!")

# The main loop
coinflip()
