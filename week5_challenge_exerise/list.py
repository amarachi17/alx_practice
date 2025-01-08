# Exercise 1
# # Creating a list to store names of fruits

# fruits = ['Apple', 'Pears', 'Orange', 'Pineapple']
# print(fruits[1])

# Exercise 2
# # Creating a dictionary to store name of your favorite book

# favorite_book = {'title': 'A tale of two cities', 'author': 'Charles Dickens', 'genre': 'Historical Fiction'}
# print(favorite_book['genre'])

# Exercise 3
# Generating a random set of numbers

import random

#  Generating a random list of numbers
random_numbers = [random.randint(1, 10) for _ in range(20)]

# Removing duplicates using sets
unique_numbers = set(random_numbers)

# Displaying the results
print("Original numbers generated: ", random_numbers)
print("Unique numbers: ", unique_numbers)