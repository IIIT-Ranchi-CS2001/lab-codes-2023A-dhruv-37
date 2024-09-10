#Calculate the fibonacci series

f = 0
s = 1

n = int(input("Enter number of terms: "))

print(f," ")
while(n):
    print(s)
    c = s
    s = f + s
    f = c
    n = n - 1