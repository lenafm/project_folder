def sum_of_even_numbers(lst):
    current_sum = 0
    for num in lst:
        if num % 2 == 0:
            current_sum += num
    return current_sum
