'''
Write a program that reads a number N and prints the average of N numbers from 1.

The average of N numbers from 1 can be calculated as,

Average = Sum of N numbers from 1 / Count of numbers (N)

Example: If N = 3, the average of 3 numbers from 1
Average = (1 + 2 + 3) / 3 = 2.0
'''
n = int(input())
c = 0
numbers = 0
while c <= n:
    numbers = (numbers + c)
    c = c + 1 
print(numbers/n)