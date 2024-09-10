#Print the multiplication table of a number upto a given limit

n = int(input("Enter the number: "))
lim = int(input("Enter upto how many terms you wish to print: "))

for i in range(lim):
    print(n,"X",i+1,"=",n*(i+1))