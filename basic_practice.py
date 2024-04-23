#Basic Practice

# Variables and Data Types

num1 = 17                # Integer variable
num2 = 3.45              # Float variable
name = "Nolan"           # String variable

# Print the values and their types

print(f"num1: {num1}, type: {type(num1)}")
print(f"num2: {num2}, type: {type(num2)}")
print(f"name: {name}, type: {type(name)}")

# User Input

age = int(input("Enter your age: "))

# Conditional logic to print messages based on age

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Function to check if a number is positive, negative, or zero

def check_number(num):
    if num > 0:
        print("Positive number.")
    elif num < 0:
        print("Negative number.")
    else:
        print("Zero.")

# Loop to print even numbers from 0 to 20

for number in range(21):  # Loop through numbers 0 to 20
    if number % 2 == 0:   # Check if the number is even
        print(number)

# Function to calculate and return the area of a circle

def calculate_circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    return area
