'''Write a program that reads two numbers A and B, and checks if one of the below conditions is satisfied.

One of A and B is less than 20.
The sum of A and B is between 30 and 50.
Print the sum of A and B if one of the given conditions is satisfied. Otherwise, print A and B on each line.'''
A = int(input())
B = int(input())
check = A < 20 or B < 20 
check2 = (A + B)
if check or (check2 > 30 and check2 < 50):
    print(check2)
else:
    print(A)
    print(B)