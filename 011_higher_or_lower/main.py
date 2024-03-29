import random
from game_data import data

def random_number():
  random_number = random.randint(0, len(data) - 1)
  return random_number

def compare_a(random_n):
  a = data[random_n]
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
  return a['follower_count']
  
def compare_b(random_n):
  b = data[random_n]
  print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
  return b['follower_count']

current_score = 0
game_continues = True

random_a = random_number()
random_b = random_number()
while random_a == random_b:
  random_b = random_number()

while game_continues:
  random_c = random_number()
  while random_c == random_a or random_c == random_b:
    random_c = random_number()

  a = compare_a(random_a)
  b = compare_b(random_b)

  if a > b:
    highest = "A"
  else:
    highest = "B"

  user_input = input("Who has more followers? Type 'A' or 'B': ")
    
  if user_input == highest:
    current_score += 1
    print(f"You're right! Current score: {current_score}")
  else:
    print(f"That was wrong. Final score: {current_score}")
    game_continues = False

  random_a = random_b
  random_b = random_c
