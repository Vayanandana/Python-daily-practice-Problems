'''
Write a program that reads two numbers A and B, and checks if both A and B are positive numbers or both A and B are less than 70.

Input
The first line of input contains an integer representing A.
The second line of input contains an integer representing B.

Output
The output should be a single line containing a boolean. True should be printed if both A and B are positive numbers or both A and B are less than 70, otherwise False should be printed.
'''
A = int(input())
B = int(input())
positive_num1 = A > 0 
positive_num2 = B > 0
check1 = ( B < 70  ) 
check2 = ( A < 70  )
compare = (positive_num1 and positive_num2) or (check1 and  check2)
print(compare)