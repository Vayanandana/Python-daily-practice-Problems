'''Write a program that reads a four-digit number and checks if the first two digits of the number are 19 and the last two digits of the number are between 30 and 60.

The input will be a single line containing a four-digit integer.

The output should be a single line containing a boolean. True should be printed if the first two digits of the number are 19 and the last two digits of the number are between 30 and 60, otherwise False should be printed.'''
num = input()
first_digit = num[0]
second_digit = num[1]
third_digit = num[2]
fouth_digit = num[3]
check_1 = int(first_digit + second_digit) == 19
check_2  = (int(third_digit + fouth_digit) > 30) and (int(third_digit + fouth_digit) < 60)
compare = check_1 and check_2
print(compare)