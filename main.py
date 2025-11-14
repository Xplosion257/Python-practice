# Imports
import random
import os

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
    elif answer == "y":
      result = random.randint(1, 2)
      if result == 2:
        coinScore += 1
      print(f"Your score was {coinScore}!")
    elif answer == "clear":
      os.system('cls' if os.name == 'nt' else 'clear')

# The main loop
coinflip()
