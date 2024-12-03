point1 = [float(x) for x in input("Enter x1 and y1: ").split()]
point2 = [float(x) for x in input("Enter x2 and y2: ").split()]

x1, y1 = point1
x2, y2 = point2

if x1 == x2:
    print(f"The equation of the line is x = {x1}")
else:
    m = (y2-y1)/(x2-x1)
    b = y1-m*x1
    print(f"The equation of the line is: y = {m}x + {b}")