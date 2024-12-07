names = [input("Enter customer name: ")for _ in range(3)]
ids = [int(input("Enter customer ID: "))for _ in range(3)]
points = [int(input("Enter shopping points: "))for _ in range(3)]

tuples_with_zip = list(zip(names,ids,points))

tuples_without_zip = [(names[i],ids[i],points[i])for i in range(len(names))]

sortedwofunc_tuple_with_zip = tuples_with_zip
n = len(tuples_with_zip)
for i in range(n):
        for j in range(0, n-i-1):
            if sortedwofunc_tuple_with_zip[j][2] > sortedwofunc_tuple_with_zip[j+1][2]:
                sortedwofunc_tuple_with_zip[j], sortedwofunc_tuple_with_zip[j+1] = sortedwofunc_tuple_with_zip[j+1], sortedwofunc_tuple_with_zip[j]

sortedfunc_tuple_with_zip = sorted(tuples_with_zip)

sortedwofunc_tuple_without_zip = tuples_without_zip
n = len(tuples_without_zip)
for i in range(n):
        for j in range(0, n-i-1):
            if sortedwofunc_tuple_without_zip[j][2] > sortedwofunc_tuple_without_zip[j+1][2]:
                sortedwofunc_tuple_without_zip[j], sortedwofunc_tuple_without_zip[j+1] = sortedwofunc_tuple_without_zip[j+1], sortedwofunc_tuple_without_zip[j]

sortedfunc_tuple_without_zip = sorted(tuples_without_zip)

print("Sorted list of tuples with zip w/o function:", sortedwofunc_tuple_with_zip)
print("Sorted list of tuples with zip with function:", sortedfunc_tuple_with_zip)

print("Sorted list of tuples w/0 zip w/o function:", sortedwofunc_tuple_without_zip)
print("Sorted list of tuples w/0 zip with function:", sortedfunc_tuple_without_zip)