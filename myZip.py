def my_zip(names, ids, points, strct=True):
    if strct:
        if len(names) == len(ids) == len(points):
            return [(names[i], ids[i], points[i]) for i in range(len(names))]
        else:
            return "Error: Lists are not of equal length"
    else:
        min_length = min(len(names), len(ids), len(points))
        return [(names[i], ids[i], points[i]) for i in range(min_length)]

customer_names = ['Alice', 'Bob', 'Carol']
customer_ids = [101, 102]
shopping_points = [150, 200, 250]

result_strict = my_zip(customer_names, customer_ids, shopping_points, strct=True)
print("Result with strct=True:", result_strict)

result_non_strict = my_zip(customer_names, customer_ids, shopping_points, strct=False)
print("Result with strct=False:", result_non_strict)
