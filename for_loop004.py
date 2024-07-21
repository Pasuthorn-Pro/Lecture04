String = (input("Enter any string: "))
modified_string = ""
Vowels = "aeiouAEIOU"

for char in String:
    upper_char = char.upper()
    if upper_char in Vowels:
        modified_string += "*"
    else:
        modified_string += upper_char

print("Modified_string: ", modified_string)