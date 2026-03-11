'''Write a program that reads a number N and prints the sum of N Natural Numbers.

Input
The input will be a single line containing an integer representing N.

Output
The output should be a single line containing an integer that is the sum of N Natural Numbers.

Explanation
For example, if the given number is N = 6,

The numbers from 1 to 6 are 1, 2, 3, 4, 5 and 6.
The sum of the numbers is 21. (1 + 2 + 3 + 4 + 5 + 6 = 21)'''

N = int(input())
c = 0
summ = 0
while c < N:
    c = c + 1
    summ = summ + c
print(summ)