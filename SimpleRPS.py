#Rock paper scissors

from random import randint 
from time import sleep

options = ["R", "P", "S"]
win = "You win!"
lose = "You lose!"
choice = {"R" : "Rock", "P" : "Paper", "S" : "Scissor"}

def winner(user_choice, comp_choice):
  if (user_choice != "R") and (user_choice != "P") and (user_choice != "S"):
    print ("Invalid Choice")
  # Tie
  elif (user_choice == comp_choice):
    print ("User chooses: %s") % (choice[str(user_choice)])
    sleep(1)
    print (".\n.\n.")
    sleep(1)
    print ("Computer chooses: %s") % (choice[str(comp_choice)])
    sleep(1)
    print (".\n.\n.")
    sleep(1)
    print ("It's a tie!")
  # Losing conditions
  elif \
  (user_choice == "R") and (comp_choice == "P") or \
  (user_choice == "P") and (comp_choice == "S") or \
  (user_choice == "S") and (comp_choice == "R"):
    print ("User chooses: %s") % (choice[str(user_choice)])
    sleep(1)
    print (".\n.\n.")
    sleep(1)
    print ("Computer chooses: %s") % (choice[str(comp_choice)])
    sleep(1)
    print (".\n.\n.")
    sleep(1)
    print lose
  # Winning Conditions
  elif \
  (user_choice == "R") and (comp_choice == "S") or \
  (user_choice == "P") and (comp_choice == "R") or \
  (user_choice == "S") and (comp_choice == "P"):
    print ("User chooses: %s") % (choice[str(user_choice)])
    sleep(1)
    print (".\n.\n.")
    sleep(1)
    print ("Computer chooses: %s") % (choice[str(comp_choice)])
    sleep(1)
    print (".\n.\n.")
    sleep(1)
    print win
  
  
    
    
    
def input():
  print "Let's Play!"
  user_choice = raw_input("Choose Rock (r), Paper (p), or Scissors (s):  ")
  user_choice = user_choice.upper()
  comp_choice = options[randint(0, 2)]
  winner(user_choice, comp_choice)
input()
  
  