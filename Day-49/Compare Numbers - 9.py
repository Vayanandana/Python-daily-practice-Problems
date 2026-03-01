num = input()
first_digit = num[0] 
second_digit = num[1]
third_digti = num[2]
check_1 = (int(first_digit) > 7) and (int(second_digit) > 7 and int(third_digti) > 7)
check_2 = (int(second_digit) * int(third_digti)) < 30
compare = check_1 or check_2
print(compare)