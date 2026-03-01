num = input()
first_digit = num[0]
second_digit = num[1]
third_digit = num[2]
check_1 = (int(first_digit) > 4 and int(second_digit) > 4) and (int(third_digit) > 4)
check_2 = int(first_digit) == 6
compare_numbers = check_1 or check_2
print(compare_numbers)