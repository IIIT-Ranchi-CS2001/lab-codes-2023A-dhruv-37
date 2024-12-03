
# Solution 3: Create lists using comprehension and construct a list of tuples

customer_names = [input(f"Enter name of customer {i+1}: ") for i in range(3)]
customer_ids = [int(input(f"Enter ID of customer {i+1}: ")) for i in range(3)]
shopping_points = [int(input(f"Enter shopping points of customer {i+1}: ")) for i in range(3)]

# Construct list of tuples without zip
list_of_tuples_manual = [(customer_names[i], customer_ids[i], shopping_points[i]) for i in range(3)]
print("List of tuples (manual):", list_of_tuples_manual)

# Construct list of tuples with zip
list_of_tuples_zip = list(zip(customer_names, customer_ids, shopping_points))
print("List of tuples (with zip):", list_of_tuples_zip)
