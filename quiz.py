```python
import random
# Tyty-lerler quiz game and more
print("Tyty-lerler presents")

# Requirements:
-Python 3.7 or higher

# Stats
def stats():
  Coins = 0
  Lives = 3
  Score = 0
  in_a_row() = 0
    if Lives = 0:
      print(GAME OVER!)
      player:kick(GAME OVER!)
      print({Coins}
            {Score})
    else:
      print()

# Get user input
name = input('What is your name?\n')


# Greet the user
def greet_user(name):
  print(f"Hello, {name}!")

greet_user(name)

# Quiz selection
print(f"{name},lets do a fun quiz.")
print("""Select your difficulty:
[Easy = *1.5 coins]
[Medium = *2 coins]
[Hard = *3 coins]
[Insane = *5 coins]
[Improbable = *8 coins + 0.5% chance for jackpot]
[Impossible = *10 coins + 1% chance for jackpot]
[God = *15 coins + 7.5% chance for 1 secret tier or higher pet]
[Demigod = *17.5 coins + 10% chance for 3 chronic tier or higher pet]
[Universally ultragod = *25 coins + 15% chance for 5 multiversal tier or higher pet]""")

# Selected difficulty
def selected_difficulty():
  difficulty = input("Select your difficulty:")
  return difficulty

# Easy difficulty
difficulty = selected_difficulty()
if difficulty == "Easy":
  num1 = random.randint(0, 10)
  num2 = random.randint(0, 20)
  question = f"{num1} + {num2} ="
  correct_answer = num1 + num2

  # Get user input
  user_input = input(question)
  if question == correct_answer:
    result = "Correct!"
    in_a_row += 1
    print(result)
  else:
    result = "Wrong! The answer was {correct_answer}."
    in_a_row = 0
    Coins -= 10
    Lives -= 1
    Score += 0
    print(result)
  except ValueError:
    print("Please enter a number.")
    in_a_row = 0
    Coins -= 10
    Lives -= 1
    Score += 0
  def in_a_row:
    if in_a_row >= 3:
      Coins * 1.5
    if in_a_row >= 5:
      Coins * 2
    else:
      Coins * 1

# Pets
def pets():
  pets = []
if difficulty == "Easy":
  if result == "Correct!":
    pets = random.randint(1, 1000000)
  else:
    pets = random.randint(0, 0)
  if pets == 1000000:
    pets = "Tyty-lerler"
    print("Tyty-lerler pet")
    storage("Tyty-lerler")
  elif pets == 999999:
    pets = "???"
    print("??? pet")
  elif pets >= 999975:
    pets = "??"
    print("?? pet")
  elif pets >= 999950:
    pets = "?"
    print("? pet")
  elif pets >= 999900:
    pets = "Exclusive"
    print("Exclusive pet)
  elif pets >= 999700:
    pets = "Thunderous"
    print("Thunderous pet")
  elif pets >= 999100:
    pets = "Multiversal"
    print("Multiversal pet")
  elif pets >= 998750:
    pets = "Chronic"
    print("Chronic pet")
  elif pets >= 998000:
    pets = "Glitch"
    print("Glitch pet")
  elif pets >= 996000
    pets = "Secret"
    print("Secret pet")
  elif pets >= 993500
    pets = "Futuristic"
    print("Futuristic pet")
  elif pets >= 980000
    pets = "Legendary"
    print("Legendary pet")
  elif pets >= 875000
    pets = "Epic"
    print("Epic pet")
  elif pets >= 700000
    pets = "Rare"
    print("Rare pet")
  elif pets >= 600000
    pets = "Uncommon"
    print("Uncommon pet")
  elif pets = 250000
    pets = "Common"
    print("Common pet")
  
    
  
