# Introduction to the casino
print("Welcome to our Totally Not Rigged Casino!")
print("My name is Nathan and I will be your host this evening")
print("")

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
