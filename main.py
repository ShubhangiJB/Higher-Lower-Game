#import
from replit import clear
import art
from game_data import data
import random

def new_influencer():
  '''get a random insta personality'''
  return random.choice(data)

def account_data(serial, acc):
  '''print account's data'''
  vowels = ["a", "e", "i", "o", "u"]
  i_name = acc['name']
  i_description = acc['description']
  article = ""
  if i_description[0].lower() in vowels:
    article = "an"
  else:
    article = "a"
  i_country = acc['country']
  comp_ag = ""
  if serial.lower()=="a":
    comp_ag = "Compare"
  else:
    comp_ag = "Against"
  
  print(f"{comp_ag} {serial}: {i_name}, {article} {i_description}, from {i_country}.")

def compare(a, b):
  '''compare the number of followers of the two celebrities.'''
  if a['follower_count']>b['follower_count']:
    return a
  else:
    return b
  
def game_play(a, curr_score):
  print(art.logo)
  if curr_score!=0:
    print(f"You're right!. Current score: {curr_score}")
  b = new_influencer()
  if a==b:
    b = new_influencer()
  account_data("A", a)
  print(art.vs)
  account_data("B", b)

  more_followed = compare(a, b)

  user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
  user_selected_celeb = {}
  if user_choice=="a":
    user_selected_celeb = a
  elif user_choice=="b":
    user_selected_celeb = b

  if user_selected_celeb!=more_followed:
    clear()
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {curr_score}")
  else:
    curr_score += 1
    clear()
    game_play(b, curr_score)
  

#choose two random objects from game data
a = new_influencer()
score = 0
game_play(a, score)
  
