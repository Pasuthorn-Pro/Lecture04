colum = int(input("Enter number of columns: "))
for i in range(1, 101):
    print(i, end=' ')
    if (i % colum) == 0:
        print()