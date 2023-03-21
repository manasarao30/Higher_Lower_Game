from game_data import data
import random
import os
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

from art import vs,logo


#Get data from random account
def random_account():
  return random.choice(data)

#Compare both the accounts 
def compare(acc1,acc2):
  print(f"Compare A: {acc1['name']}, {acc1['description']}, from {acc1['country']}")
  print(vs)
  print(f"Against B: {acc2['name']}, {acc2['description']}, from {acc2['country']}")
  return acc1,acc2

#Check the number of followers and return account name with highest follower
def follower_check(acc1,acc2):
  acc1_follower=acc1['follower_count']
  acc2_follower=acc2['follower_count']
  if acc1_follower>acc2_follower:
    ans= acc1['name']
  else:
    ans= acc2['name']
  return ans



score=0
end_of_game=False
acc1=random_account()
acc2=random_account()
if acc1==acc2:
  acc2=random_account()
print(logo)
while not end_of_game:
  outputs=compare(acc1,acc2)
  acc1=outputs[0]
  acc2=outputs[1]
  user_guess=input("Who has more followers? Type 'A' or 'B':")
  if user_guess=='A':
    user_guess=outputs[0]
    guess=user_guess['name']
  else:
    user_guess=outputs[1]
    guess=user_guess['name']
  res=follower_check(acc1,acc2)
  screen_clear()
  print(logo)
  if guess == res:
    score+=1
    acc1=acc2
    acc2=random_account()
    print(f"You're right! Current score: {score}.")
  else:
    screen_clear()
    print(f"Sorry, that's wrong. Final score: {score}")
    end_of_game=True
    
  