numbers_list = [5, 3, 8, 3, 1, 5, 9, 2, 8, 7, 1, 4, 9]
print("Original list with duplicate numbers:")
print(numbers_list)
print(f"Total elements in list: {len(numbers_list)}")
unique_numbers = set(numbers_list)
print("\nList after removing duplicates (using set):")
print(sorted(unique_numbers))
print(f"Total unique elements: {len(unique_numbers)}")
