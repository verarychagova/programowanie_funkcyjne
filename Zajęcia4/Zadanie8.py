def partition_list(lst, predicate):
    true_list = []
    false_list = []
    for item in lst:
        if predicate(item):
            true_list.append(item)
        else:
            false_list.append(item)
    return (true_list, false_list)

def is_even(number):
    return number % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers, odd_numbers = partition_list(numbers, is_even)

print("Even numbers:", even_numbers)  
print("Odd numbers:", odd_numbers)