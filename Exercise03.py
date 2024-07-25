colum = int(input("Enter number of columns: "))
count = 0

for i in range(1, 101):

    print(i, end=' ')

    count += 1

    if count == colum:

        print()
       
        count = 0

if count != 0:
    print()