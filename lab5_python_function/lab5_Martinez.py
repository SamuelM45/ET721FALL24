"""
Samuel Martinez
Sep 16, Python functions
"""

import math
import random

# Example 1: Print a message
# This is a function that doesn't return or pass a value
def hellofunction():
    print("Welcome to function!")


# Example 2: Pass a username as argument
# This function takes a username but doesn't return any value
def greeting(username):
    print(f"Good afternoon {username}")

# Example 3: Function with default parameter
# This function has a default parameter, but it doesn't return any value
def usercountry(countryname=""):
    print(f"I am from {countryname}")


# Example 4: Pass and return value
# This function returns triple the value of a given number
def triplenumber(num=0):
    return 3*num

# Example 5: Check divisibility
# This function checks if two numbers are divisible by each other.
# Returns True if divisible, otherwise False
def isdivisible(n1, n2):
    if n1 % n2 == 0 or n2 % n1 == 0:
        return True
    else:
        return False


# Example 6: Calculate circumference
# This function returns the circumference given the radius of a circle
def circumference(radius):
    return 2 * math.pi * radius


# Example 8: Roll a dice
# This function returns a random number between 1 and 6
def rolldice():
    return random.randint(1, 6)




# Function calls


# Example 1: Call a function that doesn't return or pass a value
print("\n ---- Example 1 ----- ")
hellofunction()
hellofunction()

# Example 2: Call a function that passes a username as argument
print("\n ---- Example 2 ----- ")
username = "peterpan123"
greeting(username)

# Example 3: Call a function with a default parameter
print("\n ---- Example 3: function with default parameter ----- ")
usercountry("China")
usercountry()

# Example 4: Call a function that passes a number and returns the triple of that number
print("\n ---- Example 4: function that passes a number and returns the triple of that number ----- ")
n = 9
print(f"The triple of number {n} is {triplenumber(n)}")

# Example 5: Call a function that checks if two numbers are divisible
print("\n ---- Example 5: function that passes two numbers and returns True or False ----- ")
n1 = 10
n2 = 3
check1 = isdivisible(n1, n2)
print(f"Is {n1} and {n2} divisible? {check1}")

# Example 6: Call a function that calculates the circumference of a circle
print("\n ---- Example 6: function that passes a radius and returns the circumference ----- ")
r = 5
c = circumference(r)
print(f"A circle with radius {r} has a circumference of {c:.2f}")

# Example 7: Generate random numbers
print("\n ---- Example 7: random numbers ----- ")
print(f"random number {random.random()}")
print(f"random uniform {random.uniform(-5, 5)}")
print(f"random randint {random.randint(-10, 10)}")

# Example 8: Roll a dice
print("\n ---- Example 8: roll a dice ----- ")
print(f"dice number = {rolldice()}")



# Exercise: Guess a number

def guessnumber(min_num, max_num):
    return random.randint(min_num, max_num)

def compareguess(guess_num, random_num):
    if random_num < guess_num:
        print("The number is smaller than the guess number")
    elif random_num > guess_num:
        print("The number is bigger than the guess number")
    else:
        print("You got it!")

GUESS_NUMBER = 13

print("\n ---- Exercise: Guess a number ----- ")
min_num = 1
max_num = 20
random_number = guessnumber(min_num, max_num)
print(f"Random number generated: {random_number}")
compareguess(GUESS_NUMBER, random_number)