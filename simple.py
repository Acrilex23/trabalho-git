# Simple Python Script

# Prompt the user for their name
user_name = input("Enter your name: ")

# Greet the user
print(f"Hello, {user_name}! Welcome to the world of Python scripting.")

# Prompt the user for a number
user_number = float(input("Enter a number: "))

# Calculate and print the square of the number
square_result = user_number ** 2
print(f"The square of {user_number} is: {square_result}")

# Check if the square is an even or odd number
if square_result % 2 == 0:
    print(f"The square is an even number.")
else:
    print(f"The square is an odd number.")

# Calculate and print the square root of the user's number
square_root_result = user_number ** 0.5
print(f"The square root of {user_number} is: {square_root_result}")

print("Hello World")

