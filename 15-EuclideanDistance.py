import math

x1 = int(input("Enter the x1 coordinate"))
y1 = int(input("Enter the y1 coordinate"))
z1 = int(input("Enter the z1 coordinate"))
x2 = int(input("Enter the x2 coordinate"))
y2 = int(input("Enter the y2 coordinate"))
z2 = int(input("Enter the z2 coordinate"))

xdist = x2-x1 if x2-x1 > 0 else x1-x2
ydist = y2-y1 if y2-y1 > 0 else y1-y2
zdist = z2-z1 if z2-z1 > 0 else z1-z2

sum = xdist**2 + ydist**2 + zdist**2
ans = math.sqrt(sum)

print("Distance between the two points is:",ans)