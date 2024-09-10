#Calculate the sum of digits of a number

n = int(input("Enter the number: "))
cpy = n
sum = 0;
while(n):
    rem = n % 10
    sum = sum + rem
    n = int(n / 10)

print("The sum of digits of",cpy,"is:",sum)