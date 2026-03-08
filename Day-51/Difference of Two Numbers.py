'''
Write a program that reads three numbers A, B, and C, and checks if the difference between any two numbers (A - B, B - C and C - A) is always less than 25.

Print Difference is less than 25 if the difference between any two numbers (A - B, B - C and C - A) is always less than 25. Otherwise, print Difference is not less than 25.
'''
a = int(input())
b = int(input())
c = int(input())
check1 = a - b < 25
check2 = b - c < 25
check3 = c - a < 25
if (check1 and check2) and check3:
    print("Difference is less than 25")
else:
    print("Difference is not less than 25")