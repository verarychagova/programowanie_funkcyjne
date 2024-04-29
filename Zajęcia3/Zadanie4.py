list_of_numbers = [1, 2, 3, 4, 5, 6, 7]

filtered_numbers = [square for number in list_of_numbers if (square := number ** 2) > 10]

print(filtered_numbers)