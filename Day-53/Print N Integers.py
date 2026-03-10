'''
Write a program to print integers from 1 to the given integer (N).

Input
The first line of input will contain a positive integer.

Output
The output should be of N lines, printing an integer in each line.

Explanation
For example, if the given number is 3, your code should print the

123
Similarly, if the given number is 5, your code should print the

12345

'''
n = int(input())
count = 1
while count < n + 1 :
    a = count * 1
    print(a)
    count = count + 1 