def cumulative_sum(lst):
    cumulative_list = []
    current_sum = 0
    for number in lst:
        current_sum += number
        cumulative_list.append(current_sum)
    return cumulative_list

print(cumulative_sum([1, 2, 3, 4]))