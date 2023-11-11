import pandas as pd
import json
import datetime

# Introduction to the casino

print("Welcome to our Totally Not Rigged Casino!")
print("My name is Nathan and I will be your host this evening")
print("")

'''
Objectives:
- Create a LOCAL dictionary within class Player with name and password as keys for the value of money
  that can track the player's money as they play (Done)
    + For each game the player play just assign the money value using the keys to a new variable,
      manipulate the amount as they play and then add the value back to the same keys
    
- Create a profit loss analysis for each player, each games (+ for profit and - for loss)
    + When the player switch game or cash-out record the amount of money win or lose by the player per game
    + Record the amount total win lose by the player from deposit to cash-out
    + Suggestion to use data frame from pandas to record these value 
      with the column names are the 3 games and the row names are the players (Done)

- Need to write the dictionary as well as the dataframe to a file and 
  open it everytime the script runs to add values
'''
# Read a balance sheet if existed, else create an empty one

# Get current month and year
current_date = datetime.datetime.now()
current_month = current_date.month
current_year = current_date.year

# Read the current month balance sheet. If the balance sheet doesn't exist for this month, write a new blank one
try:
    with open(f'balance_sheet_{current_month}_{current_year}.text', 'r') as file:
        balance_sheet: object = json.load(file)
except FileNotFoundError:
    # Empty profit-Loss Analysis dataframe (Global)
    balance_sheet = pd.DataFrame({'BlackJack': [],
                                  'Slot_Machine': [],
                                  'Roulette': []}
                                 )


class Player:
    def __init__(self):
        self.name = input("What is your name?: ")
        print("")
        print(f"Hello, {self.name}! ")
        print("")
        self.password = input('Please provide a unique and secure password for cash-out later: ')
        print("")
        print("Since our casino is quite new, we can only accept deposit between $100 to $2000 and no change.")
        while True:
            try:
                self.money_deposit = int(input("Enter the amount you wish to play today: "))
                while 2000 < self.money_deposit or self.money_deposit < 100:
                    self.money_deposit = int(input("The deposit doesn't meet our requirement, please input another "
                                                   "amount: "))
                break  # Break out of the loop when input an integer between 100 and 2000

            except ValueError:
                print("I'm sorry, please input the amount of money you wished to deposit: ")
        # Empty dictionary to store nested keys 'name' and 'password' for the value 'money'
        self.password_money = {self.name: {}}

    def password_money_dictionary_add(self):
        # Empty dictionary to store nested keys 'name' and 'password' for the value 'money_deposit'
        self.password_money[self.name][self.password] = self.money_deposit
        # print(f"Name: {self.name}, Password: {self.password}, Money: {self.money_deposit}")

    def add_player_balance_sheet(self):
        balance_sheet.loc[self.name] = pd.Series({col: None for col in balance_sheet.columns})

    def money_amount_checking(self):
        if self.money_deposit < 500:
            print("I hope you have a great time at our casino!")
        else:
            print("Feeling lucky today? You are surely one of the high roller in our casino!")


customer = Player()
customer.add_player_balance_sheet()
customer.money_amount_checking()
customer.password_money_dictionary_add()

# money_deposit_test = customer.password_money[customer.name][customer.password]
# print(money_deposit_test)
# print(customer.password_money)
# print(balance_sheet)

print("")
print("Your deposit is processed.")
print("Currently we are able to offer 3 games: Slot Machine, BlackJack and Roulette.")
print("")
game = input("Please choose the games that you would like to start: ")
