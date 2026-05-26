```python
import random
import time
# Tyty-lerler quiz game and more
print("Tyty-lerler presents")

# Requirements:
-Python 3.7 or higher

# Stats
def stats():
  coins = 0
  lives = 3
  score = 0
  in_a_row = 0
  global coins
  global lives
  if lives == 0:
    print(GAME OVER!)
    exit()
    print({coins}
          {score})
  else:
    print()

# Pets Storage and equip pets
pet_inventory = []
def pet_storage(pet_name):
  pet_inventory.append(pet_name)
  print(f"{pet_name} was added to your storage!")

def pet_equip(pet_name):
  pet_equip = []
  pet_equip.append(pet_name)
  print(f"Successful equipped {pet_name}{pets}!")
  if pet_equipped = "Tyty-lerler":
    if difficulty == "Easy":
      if answer(question) == correct_answer:
        coins *= 1200
        lives += 2
      if lives == 0: 
        lives += 3
        print("REVIVED!")
  if pet_equipped = "Immortal Skeletal Peagusus":
    if difficulty == "Easy":
      if answer(question) == correct_answer:
        coins *= 1000
        lives += 1
      if lives == 0:
        lives += 2
        print("REVIVED!")
  if pet_equipped = "Voided Knight Unicorn":
    if difficulty == "Easy":
      if answer(question) == correct_answer:
        coins *= 1000
        lives += 2
      if lives == 0:
        lives += 2
        print("REVIVED!")

# Get user input
name = input('What is your name?\n')


# Greet the user
def greet_user(name):
  print(f"Hello, {name}!")

greet_user(name)

# Quiz selection
print(f"{name},lets do a fun quiz.")
print("""Select your difficulty:
[Easy *= 1.5 coins]
[Medium *= 2 coins]
[Hard *= 3 coins]
[Insane *= 5 coins]
[Improbable *= 8 coins + 0.5% chance for jackpot]
[Impossible *= 10 coins + 1% chance for jackpot]
[God *= 15 coins + 7.5% chance for 1 secret tier or higher pet]
[Demigod *= 17.5 coins + 10% chance for 3 chronic tier or higher pet]
[Universally ultragod *= 25 coins + 15% chance for 5 multiversal tier or higher pet]""")

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
  start_time = time.time()
  
  # Get user input
  def answer():
    user_input = input(question)
    input(question) = input(f"{num1} + {num2}")
  end_time = time.time()
  time_taken = end_time - start_time
  print(f"You took {time_taken} seconds!")
  if answer(question) == correct_answer:
    result = "Correct!"
    in_a_row += 1
    print(result)
  else:
    result = "Wrong! The answer was {correct_answer}."
    in_a_row = 0
    coins -= 10
    lives -= 1
    score += 0
    print(result)
 try:
     user_input = int(input(question))  
 except ValueError:
    print("Please enter a number.")
    in_a_row = 0
    coins -= 10
    lives -= 1
    score += 0
  def in_a_row:
    if in_a_row >= 3:
      coins *= 1.5
    if in_a_row >= 5:
      coins *= 2
    else:
      coins *= 1

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
    pet_name = "Tyty-lerler"
    print("Tyty-lerler pet")
    pets_storage("Tyty-lerler")
  elif pets == 999999:
    pets = "???"
    pet_name = random.randint(1, 4)
    if pet_name == 1:
      pet_name = "Immortal Skeletal Peagusus"
      print("Immortal Skeletal Peagusus")
      pet_storage("Immortal Skeletal Peagusus")
    if pet_name == 2:
      pet_name = "Voided Knighted Unicorn"
      print("Voided Knighted Unicorn")
      pet_storage("Voided Knighted Unicorn")
    if pet_name == 3:
      pet_name = "Hurricane Buddha Raptor"
      print("Hurricane Buddha Raptor")
      pet_storage("Hurricane Buddha Raptor")
    if pet_name == 4:
      pet_name = "Crimson Awakened Semi-cat"
      print("Crimson Awakened Semi-cat")
      pet_storage("Crimson Awaken Semi-cat")
  elif pets >= 999975:
    pets = "??"
    print("?? pet")
    pet_name = random.randint(1, 4)
    if pet_name == 1:
      pet_name = "Crypto Historical UltraDog"
      print("Crypto Historical UltraDog")
      pet_storage("Crypto Historical UltraDog")
    if pet_name == 2:
      pet_name = "Crypto Historical UltraCat"
      print("Crypto Historical UltraCat")
      pet_storage("Crypto Historical UltraCat")   
    if pet_name == 3:
      pet_name = "Bitcoin Historical UltraFox"
      print("Bitcoin Historical UltraFox")
      pet_storage("Bitcoin Historical UltraFox")    
    if pet_name == 4:
      pet_name = "Teleporting Historical MegaFrog"
      print("Teleporting Historical MegaFrog")
      pet_storage"Teleporting Historica MegaFrog")
  elif pets >= 999950:
    pets = "?"
    print("? pet")
  elif pets >= 999900:
    pets = "Exclusive"
    print("Exclusive pet")
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
  elif pets >= 996000:
    pets = "Secret"
    print("Secret pet")
  elif pets >= 993500:
    pets = "Futuristic"
    print("Futuristic pet")
  elif pets >= 980000:
    pets = "Legendary"
    print("Legendary pet")
  elif pets >= 875000:
    pets = "Epic"
    print("Epic pet")
  elif pets >= 700000:
    pets = "Rare"
    print("Rare pet")
    pet_name = random.randint(1, 7)
    if pet_name == 1:
      pet_name = "Radiated Buck"
      print("Radiated Buck")
      pet_storage("Radiated Buck")
    if pet_name == 2:
      pet_name = "Firey Otter"
      print("Firey Otter")
      pet_storage("Firey Otter")
    if pet_name == 3:
      pet_name = "Natural Grizzly"
      print("Natural Grizzly")
      pet_storage("Natural Grizzly")
    if pet_name == 4:
      pet_name = "Nocturnal Giraffe"
      print("Nocturnal Giraffe")
      pet_storage("Nocturnal Giraffe")
    if pet_name == 5:
      pet_name = "Normal Dodo"
      print("Normal Dodo")
      pet_storage("Normal Dodo")
    if pet_name == 6:
      pet_name = "Flying Fox "
      print("Flying Fox")
      pet_storage("Flying Fox")
    if pet_name == 7:
      pet_name = "Half Quarter-Kitten"
      print("Half Quarter Kitten")
      pet_storage("Half Quarter Kitten")
  elif pets >= 600000:
    pets = "Uncommon"
    print("Uncommon pet")
    pet_name = random.randint(1, 7)
    if pet_name == 1:
      pet_name = "Normal Duck"
      print("Normal Duck")
      pet_storage("Normal Duck")
    if pet_name == 2:
      pet_name = "Normal Elephant"
      print("Normal Elephant")
      pet_storage("Normal Elephant")
    if pet_name == 3:
      pet_name = "Normal Wolf"
      print("Normal Wolf")
      pet_storage("Normal Wolf")
    if pet_name == 4:
      pet_name = "Normal Giraffe"
      print("Normal Giraffe")
      pet_storage("Normal Giraffe")
    if pet_name == 5:
      pet_name = "Normal Goat"
      print("Normal Goat")
      pet_storage("Normal Goat")
    if pet_name == 6:
      pet_name = "Normal Dove"
      print("Normal Dove")
      pet_storage("Normal Dove")
    if pet_name == 7:
      pet_name = "Normal Deer"
      print("Normal Deer")
      pet_storage("Normal Deer")
  elif pets >= 250000:
    pets = "Common"
    print("Common pet")
    pet_name = random.randint(1, 6)
    if pet_name == 1:
      pet_name = "Normal Cat"
      print("Normal Cat")
      pet_storage("Normal Cat")
    if pet_name == 2:
      pet_name = "Normal Dog"
      print("Normal Dog")
      pet_storage("Normal Dog")
    if pet_name == 3:
      pet_name = "Normal Ant"
      print("Normal Ant")
      pet_storage("Normal Ant")
    if pet_name == 4:
      pet_name = "Normal Hamster"
      print("Normal Hamster")
      pet_storage("Normal Hamster")
    if pet_name == 5:
      pet_name = "Normal Mole"
      print("Normal Mole")
      pet_storage("Normal Mole")
    if pet_name == 6:
      pet_name = "Normal Pidgeon"
      print("Normal Pidgeon")
      pet_storage("Normal Pidegon")

   
    
  
    
  
