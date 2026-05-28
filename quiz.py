```python
import random
import time
item_used = None
pet_equipped = None
potion_used = None
shop_items = None
luck_potion_multiplier = 1
coin_multiplier = 1
multiplier = 1
xp = 0
rarity_multiplier = 1
level = 1
luck = 1
coins = 0
lives = 3
score = 0
in_a_row = 0
# Tyty-lerler quiz game and more
print("Tyty-lerler presents")

# Requirements:
# Python 3.7 or higher

# Stats
def stats():
  global multiplier
  global xp
  global level
  global coins
  global lives
  global luck
  print(f"Coins: {coins}")
  print(f"Score: {score}") 
  print(f"Lives: {lives}") 
  print(f"XP: {xp}")
  print(f"Level: {level}") 
  print(f"Luck: {luck}")
  if lives == 0: 
    print("GAME OVER!")
    print(f"Coins: {coins}")
    print(f"Score: {score}")
    exit()
  else:
    print()

# Shop items

shop = {"shop_item_1": {"shop_item_name": ["legendary_pet: "coins": 10000"]}, "shop_item_2": {"shop_item_name": ["futuristic_pet: "coins": 50000"]}, "shop_item_3": {"luck_potion_1": "coins": 100000}

# Rarities

pets = {"common_pet": {"pet_name": ["Normal Cat", "Normal Dog", "Normal Ant", "Normal Hamster", "Normal Mole", "Normal Pidgeon", "pet_multiplier": 1.5]} "uncommon_pet": {"pet_name": ["Normal Duck", "Normal Elephant", "Normal Wolf", "Normal Giraffe", "Normal Goat", "Normal Dove", "Normal Deer", "pet_multiplier": 3]} "rare_pet": {"pet_name":  ["Radiated Buck", "Firey Otter", "Natural Grizzly", "Nocturnal Giraffe", "Normal Dodo", "Flying Fox", "Half Quarter Kitten" "pet_multiplier": 10]} "epic_pet": {"pet_name": ["Glacial Phoenix", "Scorching Ivory Mammoth", "Guardian Devil", "Terror MX-47", "Normal Vaquita", "pet_multiplier": 50]} "legendary_pet": {"pet_name": ["Fouled Vaquita", "Erratic Pangolin", "Cyber GI-210 Electro Phoenix", "Matrix PD-391 Fox", "pet_multiplier": 150]} "futuristic_pet": {"pet_name": ["Futuristic Vaquita", "Futuristic Woolly Mammoth", "Futuristic Hawk", "Futuristic Steampunk Monkey", "pet_multiplier": 200]} "secret_pet": {pet_name: "Reincarnated Giga-Phoenix", "Cybernetic KD-35 Hawk", "Non-binary Coded Saber-toothed Cat" "pet_multiplier": 300} "glitch_pet": {"pet_name": ["Ultra Glitched Crow", "Dark Matter Horse", "Hacked Prototype MK-56 Teleporting Chicken", "Prototype MK-57 Fennec Fox" "pet_multiplier": 350]} "chronic_pet": {"pet_name": ["Peagusus In Galaxy: Model v3.142 (P.I.G)", "Kyawthuite Mystic Dragon", "Kyanite Prototype OS-46 King Cobra", "Iridium Ore Mining Python" "pet_multiplier": 400]} 

"multiversal_pet": {"pet_name": ["Peagusus Prototype PX-12 (Module Overclocking)", "Los Angeles UltraUniverse


        






"ultra_secret_pet": {"pet_name": ["Immortal Skeletal Peagusus", "Voided Knighted Unicorn", "Hurricane Buddha Raptor", "Crimson Awakened Semi-cat", "pet_multiplier": 1500]}

# Potions
if luck_potion_multiplier += 1:
  luck *= 2
luck_potions = {"luck_potion_1": {"potion_name": ["Luck Potion I", "luck_potion_multiplier": 1.5]}} {"luck_potion_2": {"potion_name": ["Luck Potion II", "luck_potion_multiplier": 3.5]}} {"luck_potion_3": {"potion_name": ["Luck Potion III", "luck_potion_multiplier": 6.5]}} {"luck_potion_4": {"potion_name": ["Luck potion IV", "luck_potion_multiplier": 10]}} {"luck_potion_5": {"potion_name": ["Luck Potion V", "luck_potion_multiplier": 25]}}

# Shop
shop = []
items = []
def store(shop_items):
  shop_item_name = {coins} coins
  item_bought -= {coins} coins
  if level >= 2:
    shop.append(shop_item_1)
    shop_item_1 = "shop_item_name"
    print("Unlocked shop slot 1!")
  if level >= 10:
    shop.append(shop_item_2)
    shop_item_2 = "shop_item_name"
    print("Unlocked shop slot 2!")
  if shop_item_name == item_bought:
    items.append(shop_item_name)
    shop_item_name -= {coins} coins
    print(f"Successfully bought {shop_item_name}!")
  else:
    print()
  
# Pets Storage and equip pets
pet_inventory = []
def pet_storage(pet_name):
  pet_inventory.append(pet_name)
  print(f"{pet_name} was added to your storage!")

def pet_equip(pet_name):
  global pet_equipped
  if coin_multiplier += 1:
    coins *= 2 
  coin_multiplier = {"common_pet": 1.5, "uncommon_pet": 3, "rare_pet": 10, "epic_pet": 50, "legendary_pet": 150, "futuristic_pet": 200, "secret_pet": 300, "glitch_pet": 350, "chronic_pet": 400, "multiversal_pet": 500, "thunderous_pet": 550, "exclusive_pet": 600, "very_secret_pet": 700, "super_secret_pet": 1000, "ultra_secret_pet": 1500, "Tyty-lerler_pet": 2500}
  pet_equipped = pet_name
  print(f"Successful equipped {pet_name}!")
  if pet_equipped == "Tyty-lerler_pet":
    rarity_stats = {"coin_multiplier": 2500, "revive": 3, "luck" : 50, "bonus_score": 2, "xp_multiplier": 25}  

def use_potion(potion_name):
  global potion_used
  if potion_used == luck_potion_1:
    luck_potion_multiplier = 1.5
  if potion_used == luck_potion_2:
    luck_potion_multiplier = 3.5
  if potion_used == luck_potion_3:
    luck_potion_multiplier = 6.5
  if potion_used == luck_potion_4:
    luck_potion_multiplier = 10
  if potion_used == luck_potion_5:
    luck_potion_multiplier = 25
    
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
  while lives > 0:
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 20)
      
    question = f"{num1} + {num2} ="
    correct_answer = num1 + num2
      
    start_time = time.time()

    user_input = int(input(question))
      
    end_time = time.time()
      
  # Get user input
try:
     time_taken = end_time - start_time
     print(f"You took {time_taken} seconds!")
  
    if user_input == correct_answer:
      result = "Correct!"
      in_a_row += 1
      coins += 50
      lives -= 0
      score += 1
      xp += 50
      print(result)
    else:
      result = f"Wrong! The answer was {correct_answer}."
      in_a_row = 0
      coins -= 10
      lives -= 1
      score += 0
      xp += 0
      print(result)
    
except ValueError:
    print("Please enter a number.")
    in_a_row = 0
    coins -= 10
    lives -= 1
    score += 0
    xp += 0

  def streak_bonus():
    global coins
    global xp
    global in_a_row
    global luck
    
    if user_input == correct_answer:
      in_a_row += 1
    else:
      in_a_row = 0
      coins *= 1
      xp *= 1
      luck *= 1
      
    if in_a_row >= 10:
      coins *= 5
      xp *= 5
      luck *= 5   
    elif in_a_row >= 5:
      coins *= 2
      xp *= 2
      luck *= 2
    elif in_a_row >= 3:
      coins *= 1.5
      xp *= 1.5
      luck *= 1.5

  def level():
    global rarity_multiplier
    global xp
    global level
    global luck
    if xp >= 1000:
      level += 1
      luck *= 1.1
      rarity_multiplier *= 1.01
      coins += 1000
      print(f"Congrats! You are now level {level}!")

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
    pet_storage("Tyty-lerler")
    return pet_name
  elif pets == 999999:
    pets = "???"
    pet_name = random.choice(ultra_secret_pet)
    pet_storage(pet_name)
    return pet_name
  elif pets >= 999975:
    pets = "??"
    print("?? pet")
    pet_name = random.choice(super_secret_pet)
    pet_storage(pet_name)
    return pet_name
  elif pets >= 999950:
    pets = "?"
    print("? pet")
    pet_name = random.choice(very_secret_pet)
    pet_storage(pet_name)
    return pet_name
  elif pets >= 999900:
    pets = "Exclusive"
    print("Exclusive pet")
    pet_name = random.choice(exclusive_pet)
    pet_storage(pet_name)
    return pet_name
  elif pets >= 999700:
    pets = "Thunderous"
    print("Thunderous pet")
    pet_name = random.choice(thunderous_pet)
    pet_storage(pet_name)
    return pet_name
  elif pets >= 999100:
    pets = "Multiversal"
    print("Multiversal pet")
    pet_name = random.choice(multiversal_pet)
    pet_storage(pet_name)
    return pet_name
  elif pets >= 998750:
    pets = "Chronic"
    print("Chronic pet")
    pet_name = random.choice(chronic_pet)
    pet_storage(pet_name)
    return pet_name
  elif pets >= 998000:
    pets = "Glitch"
    print("Glitch pet")
    pet_name = random.choice(glitch_pet)
    pet_storage(pet_name)
    return pet_name
  elif pets >= 996000:
    pets = "Secret"
    print("Secret pet")
    pet_name = random.choice(secret_pet)
    pet_storage(pet_name)
    return pet_name
  elif pets >= 993500:
    pets = "Futuristic"
    print("Futuristic pet")
    pet_name = random.choice(futuristic_pet)
    pet_storage(pet_name)
    return pet_name
  elif pets >= 980000:
    pets = "Legendary"
    print("Legendary pet")
    pet_name = random.choice(legendary_pet)
    pet_storage(pet_name)
    return pet_name
  elif pets >= 875000:
    pets = "Epic"
    print("Epic pet")
    pet_name = random.choice(epic_pet)
    pet_storage(pet_name)
    return pet_name
  elif pets >= 700000:
    pets = "Rare"
    print("Rare pet")
    pet_name = random.choice(rare_pet)
    pet_storage(pet_name)
    return pet_name
  elif pets >= 600000:
    pets = "Uncommon"
    print("Uncommon pet")
    pet_name = random.choice(uncommon_pet)
    pet_storage(pet_name)
    return pet_name
  elif pets >= 250000:
    pets = "Common"
    print("Common pet")
    pet_name = random.choice(common_pet) 
    pet_storage(pet_name)
    return pet_name
    

   
    
  
    
  
