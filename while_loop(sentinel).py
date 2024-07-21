def print_asterisks(rows, cols):
    for i in range(rows):
        for j in range(cols):
            print('*', end=' ')
        print()

# Taking input for rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Call the function to print asterisks
print_asterisks(rows, cols)