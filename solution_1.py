
# Solution 1: Equation of a straight line passing through two points (from user input using comprehension)

# Get coordinates from user using list comprehension
x1, y1 = [float(i) for i in input("Enter the coordinates of the first point (x1, y1): ").split()]
x2, y2 = [float(i) for i in input("Enter the coordinates of the second point (x2, y2): ").split()]

# Calculate the equation of the straight line using the formula
slope = (y2 - y1) / (x2 - x1)
equation = f"(x - {x1}) = {slope}(y - {y1})"
print("The equation of the line is:", equation)
