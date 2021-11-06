# Tasks
# Create a program that will ask for the pocket money and amount of apples.
# Compute the maximum apple and remaining money of the consumer.
# Display the "You can buy ______ apples and your change is ____ pesos.")


def get_money_apple():
    Amount_money = int(input("Amount of money that you have? "))
    Price_Apple = int(input("What is the price of an apple? "))
    return Amount_money, Price_Apple


def max_apple(Pocket_money, Cost_Apple):
    maximum_apple = int(Pocket_money / Cost_Apple)
    return maximum_apple


def remaining_money(Pocket_money, apple, Cost_Apple):
    remaining_money = int(Pocket_money - (apple * Cost_Apple))
    return remaining_money


def display(apple, change):
    print(f"You can buy {apple} apples and your change is {change} pesos.")


# Ask for the pocket money and amount of apples.
Pocket_money, Cost_Apple = get_money_apple()
# Get the maximum apples.
apple = max_apple(Pocket_money, Cost_Apple)
# Get the remaining money.
change = remaining_money(Pocket_money, apple, Cost_Apple)
# Display the output
display(apple, change)
