# Count the number of occurrences of a character in a string

s = input("Enter the string: ")
ch = input("Enter the character: ")

cnt = 0

for i in s:
    if i == ch:
        cnt = cnt + 1

print("Number of occurrences of the character",ch,"in",s,"is:",cnt)