#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.
  play="Y"
  player = ""
 
   #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.
  
  while play=="Y":
    player=input("Enter choice (R/P/S):")
    
    computer=random.choice( ["R","P","S"])
    
    
    if player =="R":
        print ("Player chose Rock")
    elif player=="P":
      print ("Player chose paper")
    elif player=="S":
      print("Player chose scissors")
    else:
      print("Invalid option")

    if player==computer:
        print("tie")
        
    elif player=="R" and computer =="S":
        print("You win!")
      
    elif player=="R" and computer =="P":
        print("You lose.")
      



      #In the end, print the stats
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print("win", "\t", "tie", "\t", "lose")

if __name__ == '__main__':
  main()
