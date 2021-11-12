# Tasks
# Create a program that will ask for the number of apples and oranges.
# Compute the total amount that consumer bought.
# Display the total amount of the bought items.
# The total amount is __________.

def num_apples_oranges():
    num_apples = int(input("Suki, Ilang apple ang gusto mo? "))
    num_oranges = int(input("Suki, Bumili kana din ng orange? "))
    return num_apples, num_oranges


def total_amount(apple, orange):
    return int((apple * 20) + (orange * 25))


# Ask the consumer the number of apples and oranges
num_apples, num_oranges = num_apples_oranges()
# Compute and output the total amount
total = total_amount(num_apples, num_oranges)
# Display the apple and orange.
print(f"The total amount is {total}. ")
