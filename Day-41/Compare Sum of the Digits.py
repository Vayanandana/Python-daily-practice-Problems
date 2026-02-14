'''
Question: Compare Sum of the Digits
In this coding question, you need to write a program that reads a two-digit number N and checks if the sum of its digits is greater than 7. The input will be a single line containing a two-digit integer. 
The output should be a single line containing a boolean value, True if the sum of the digits is greater than 7, and False otherwise.
'''
N = input()
sum_two_digit = int(N[0]) + int(N[1])
compare = sum_two_digit > 7
result = compare
print(result)