# Program to print a mirrored right-angled triangle

# Take the number of rows as input from the user
n = int(input("Enter the number of rows: "))

# Loop through each row from 1 to n
for i in range(1, n + 1):
    # Print spaces followed by stars
    # For row i, we need (n - i) spaces and i stars
    print(" " * (n - i) + "*" * i)
