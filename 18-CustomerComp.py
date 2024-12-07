names = [input("Enter customer name: ")for _ in range(3)]
ids = [int(input("Enter customer ID: "))for _ in range(3)]
points = [int(input("Enter shopping points: "))for _ in range(3)]

tuples_with_zip = list(zip(names,ids,points))

tuples_without_zip = [(names[i],ids[i],points[i])for i in range(len(names))]

print("List of tuples with zip:", tuples_with_zip)
print("List of tuples without zip:", tuples_without_zip)