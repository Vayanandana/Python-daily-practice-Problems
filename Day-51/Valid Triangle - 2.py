'''In this coding question, you need to write a program that reads the three angles A, B, and C of a triangle and checks if the sum of the three angles of the triangle is equal to 180.
If the sum is equal to 180, you need to print a triangle as shown below:

*
**
***
If the sum is not equal to 180, you need to print Not a Valid Triangle.'''
A = int(input())
B = int(input())
C = int(input())
Sum = A + B + C 
if Sum == 180:
    print("*")
    print("**")
    print("***")
else:
    print("Not a Valid Triangle")