'''
Docstring for Day-37.basic-arithmetic
The program is designed to take two integer inputs, A and B, and perform three operations: addition, subtraction, and multiplication.

Logical Approach:

Read Input:
Read two integer inputs, A and B, using the input() function.

Perform Addition:
Add the values of A and B and print the result.

Perform Subtraction:
Subtract the value of B from A and print the result.

Perform Multiplication:
Multiply the values of A and B and print the result.

Example for Clarity:

If the inputs are A = 4 and B = 3:
Addition: 4 + 3 = 7
Subtraction: 4 - 3 = 1
Multiplication: 4 * 3 = 12

'''
num1= int(input())
num2 = int(input())
ADD = num1 + num2
SUB = num1 - num2
MUL = num1 * num2
print(ADD)
print(SUB)
print(MUL)