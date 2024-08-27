keep_going = "y"
while keep_going == "y":
    wholesale_cost = float(input("Enter the amount of sales: "))

    retail = wholesale_cost*2.5 

    print(f"The retail price is ${retail:.2f}")

    keep_going = input('Do you have another' /+
                       ' item (Enter y for yes): ')