def numbers_searching(*args):
    result = []
    missing_num_list = []
    numbers = (args)
    nums_and_occurances = {}
    for num in numbers:
        if num not in nums_and_occurances:
            nums_and_occurances[num] = 0
        nums_and_occurances[num] += 1
        missing_num_list.append(num)
    missing_num_list = sorted(missing_num_list)
    duplicated_numbers = []
    all_nums = set([x for x in range(missing_num_list[0], missing_num_list[-1] + 1)])
    missing_num_list = set(missing_num_list)
    missing_number = missing_num_list ^ set(all_nums)
    missing_number = missing_number.pop()
    nums_and_occurances_sorted = sorted(nums_and_occurances.items())
    for num, occurances in nums_and_occurances_sorted:
        if occurances > 1:
            duplicated_numbers.append(num)
    return [missing_number, duplicated_numbers]


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))