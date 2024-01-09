#wap to make a game of rock paper scissor in which there are 3 opponent computers
import random


#python program for a ssimple game of rock paper scissor

options = ["rock","paper","scissor"]
#enter message
name = input("Enter your name")
print(name,"\n Welcome to the game of rock paper scissor")

#code for the player
for i in options:
    print(i)

player_choice  = input("Enter your choice: ")

#code for computer choice

computer_choice = random.randint(1,3)
if computer_choice == 1:
    print("computer has choosen rock ")
elif computer_choice == 2:
    print("Computer has choosen Paper ")
elif computer_choice == 3:
    print("computer has choosen Scissor ")

#checking argument

if ( player_choice == computer_choice):
    print("The game has tied , try again")
elif (player_choice== "rock" and computer_choice == 3) or (player_choice == "paper" and computer_choice == 1) or (player_choice == "scissor" and computer_choice == 1):
    print(name," Wins")
elif (computer_choice == 1 and player_choice == "scissor") or (computer_choice == 2 and player_choice == "rock") or (computer_choice == 3 and player_choice == "paper"):
    print("Computer Wins")
print("Thanks for playing the game")