import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

print("Welcome to the PyPassword Generator!")

#The following: check that the desired # of characters is available in the list, select a random character from the list, and append it into the password list.
num_letters = int(input("How many letters would you like in your password?\n"))
if num_letters <= len(letters):
    for letter in range(num_letters):
        password.append(random.choice(letters))
else:
    num_letters= int(input("Less than 53 please.\n")) 

num_symbols = int(input(f"How many symbols would you like?\n"))
if num_symbols <= len(symbols):
    for symbol in range(num_symbols):
        password.append(random.choice(symbols))
else:
    num_symbols = int(input(f"Less than 11 please.\n"))

num_numbers = int(input(f"How many numbers would you like?\n"))
if num_numbers <= len(numbers):
    for number in range(num_numbers):
        password.append(random.choice(numbers))
else:
    num_numbers = int(input(f"Less than 11 please.\n"))

#Shuffles the order of the password list and joins them into one string.
random.shuffle(password)
password = ''.join(password)

print(f"Your password is {password}.")