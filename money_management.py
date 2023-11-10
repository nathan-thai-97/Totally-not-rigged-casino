# Introduction to the casino
print("Welcome to our Totally Not Rigged Casino!")
print("My name is Nathan and I will be your host this evening")
print("Currently we are able to offer 3 games: Slot Machine, BlackJack and Roulette")
print("")

# Collect name
name = input("What is your name?: ")
print("")
print(f"Hello, {name}! ")

print("")
print("Since our casino is quite new, we can only accept deposit between $100 to $2000")

# Collect amount of money deposit that must be a number between 100 and 2000
while True:
    try:
        money = int(input("Enter the amount you wish to play today: "))
        while 2000 < money or money < 100:
            money = int(input("The deposit doesn't meet our requirement, please input another amount: "))
        break  # Break out of the loop if conversion to int is successful

    except ValueError:
        print("I'm sorry, please input the amount of money you wished to deposit")

# while money > 2000 or money < 100:
#     money = int(input("The deposit doesn't meet our requirement, please input another amount: "))

# If condition to comment on how much they deposit
if money < 500:
    print("I hope you have a great time at our casino!")
else:
    print("Feeling lucky today? You are surely one of the high roller in our casino!")

game = input("Your deposit is processed. Please choose the games that you would like to start: ")



