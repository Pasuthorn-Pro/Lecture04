colum = int(input("Enter number of columns: "))
count = 0

for num in range(1, 101):

    print(num, end=' ')

    count += 1

    if count == colum:

        print()
       
        count = 0

if count != 0:
    print()