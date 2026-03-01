num = input()
first_digit = num[0]
second_digit = num[1]
third_digit = num[2]
check_1 = (int(second_digit) == 1) or (int(first_digit) == 1)
check_2 = (int(first_digit) + int(second_digit) + int(third_digit)) < 12
check_3 = int(third_digit) == 5
compare_numbers = (check_1 and check_2) and check_3
print(compare_numbers)