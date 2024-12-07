# Check whether all the characters in a string is alphanumeric or not

s = (input("Enter the string: "))

check = True

for i in s:
    if i.isalnum() == 0 :
        check = False
        break

if check :
    print("All the characters in the string are alphanumeric")
else :
    print("All the characters in the string are not alphanumeric")