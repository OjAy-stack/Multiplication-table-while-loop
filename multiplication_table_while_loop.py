# Prompt the user to enter any number
number = int(input("Enter a number to see its multiplication table: "))

# Initialize the counter
i = 1

# Print the multiplication table using a while loop. Here it loops through 1 to 12 for the input number.
while i <= 12:
    print(f"{number} x {i} = {number * i}")
    i += 1  # Increment the counter
