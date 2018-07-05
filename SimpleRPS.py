#Simple Rock paper scissor game!

from random import randint 
from time import sleep

#universal vars
options = ["R", "P", "S"]
win = "You win!\n"
lose = "You lose!\n"
tie = "It's a tie!\n"
choice = {"R" : "Rock", "P" : "Paper", "S" : "Scissor"}

#choosing winner
def winner(user_choice, comp_choice):
  if (user_choice != "R") and (user_choice != "P") and (user_choice != "S") and (user_choice != "Q"):
    print ("Invalid Choice\nTry Again!\n")
    input()
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
    print tie
    input()
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
    input()
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
    input()
    
  #Quit
  else:
    print "Quitting Program"
    sleep(1)
    print (".\n.\n.")
    sleep(1)
    print "Goodbye!"
    
#User input    
def input():
  print "Let's Play!"
  user_choice = raw_input("Choose Rock (r), Paper (p), or Scissors (s) or Quit (q): ")
  user_choice = user_choice.upper()
  comp_choice = options[randint(0, 2)]
  winner(user_choice, comp_choice)
input()
