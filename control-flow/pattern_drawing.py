# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a variable to track the current row
row = 0

# Use a while loop to iterate through each row
while row < size:
    # Use a for loop to print asterisks side by side for each column
    for _ in range(size):
        print("*", end="")
    
    # After printing a row of asterisks, print a newline to move to the next row
    print()
    
    # Increment the row counter
    row += 1
