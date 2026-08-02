def dupicate():
    my_list = [1, 2, 3, 4, 5, 1, 2, 6]
    duplicates = []
    for item in my_list:
        if my_list.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

duplicate_values = dupicate()
if duplicate_values:
    print(f"Duplicate values found: {duplicate_values}")
else:
    print("No duplicate values found.", duplicate_values)