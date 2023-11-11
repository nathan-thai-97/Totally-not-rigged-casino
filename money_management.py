# Introduction to the casino
import pandas

print("Welcome to our Totally Not Rigged Casino!")
print("My name is Nathan and I will be your host this evening")
print("")

'''
Objectives:
- Create a dictionary with name and password as keys for the value of money
  that can track the player's money as they play 
    + For each game the player play just assign the money value using the keys to a new variable,
      manipulate the amount as they play and then add the value back to the same keys
    
- Create a profit loss analysis for each player, each games (+ for profit and - for loss)
    + When the player switch game or cash-out record the amount of money win or lose by the player per game
    + Record the amount total win lose by the player from deposit to cash-out
    + Suggestion to use data frame from pandas to record these value 
      with the column names are the 3 games and the row names are the players
'''

import pip



balance_sheet = {}


class Player:
    def __init__(self):
        self.name = input("What is your name?: ")
        print("")
        print(f"Hello, {self.name}! ")

        print("")
        print("Since our casino is quite new, we can only accept deposit between $100 to $2000.")
        while True:
            try:
                self.money = int(input("Enter the amount you wish to play today: "))
                while 2000 < self.money or self.money < 100:
                    self.money = int(input("The deposit doesn't meet our requirement, please input another amount: "))
                break  # Break out of the loop if conversion to int is successful

            except ValueError:
                print("I'm sorry, please input the amount of money you wished to deposit: ")

    def balance_sheet_add(self):
        balance_sheet[self.name] = self.money

    def money_amount_checking(self):
        if self.money < 500:
            print("I hope you have a great time at our casino!")
        else:
            print("Feeling lucky today? You are surely one of the high roller in our casino!")


Valuable_customer = Player()
Valuable_customer.balance_sheet_add()
Valuable_customer.money_amount_checking()
print("")
print("Your deposit is processed.")
print("Currently we are able to offer 3 games: Slot Machine, BlackJack and Roulette.")
print("")
game = input("Please choose the games that you would like to start: ")
