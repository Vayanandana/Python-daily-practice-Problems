'''Write a program to check if the given two-digit number is greater than 25 and its first digit is greater than its second digit.

Input: The first line of the input will be a two-digit integer.

Output: Print "True" if the number is greater than 25 and its first digit is greater than its second digit. In all other cases print "False".

Example: When the given number is 24, it is not greater than 25 and the first digit is not greater than the second digit (2 is less than 4). When the given number is 42, it is greater than 25 and the first digit is greater than the second digit (4 is greater than 2).'''
num = input()
first_digit = num[0]
second_digit = num[1]
check1 = int(num) > 25 
check2 = int(first_digit) > int(second_digit)
compare = check1 and check2
print(compare)