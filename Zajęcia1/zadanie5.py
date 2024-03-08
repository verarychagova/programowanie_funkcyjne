def even_numbers(numbers_list):
    even = []
    for number in numbers_list:
        if number % 2 == 0:
            even.append(number)
    return even


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = even_numbers(numbers_list)
print(res)

rectangle_area = lambda length, width: length * width

length = 5
width = 10
print((rectangle_area(length, width)))