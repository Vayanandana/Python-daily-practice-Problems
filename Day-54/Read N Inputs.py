'''
Given an integer N, write a program which reads N inputs and prints them.

Input:

The first line of input will contain a positive integer, N.
The following N lines will contain an integer in each line.

Output:

The output should be N lines, containing an integer per line.
'''
n = int(input())
c = 0
while c < n:
    num = int(input())
    print(num)
    c = c + 1