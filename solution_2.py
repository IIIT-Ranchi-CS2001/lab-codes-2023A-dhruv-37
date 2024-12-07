
# Solution 2: Count the number of each character present in a string using dictionary

string = input("Enter a string: ")
char_count = {char: string.count(char) for char in string}
print("Character frequency:", char_count)
