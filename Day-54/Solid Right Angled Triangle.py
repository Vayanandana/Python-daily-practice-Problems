'''
Given an integer number (N) as input, write a program to print the right-angled triangular pattern of N lines using an asterisk(*) character.

Input: The first line of input will contain a positive integer.

Output: The output should be N lines with an asterisk() character printing in a right-angled triangular pattern. Note: There is a space after each asterisk() character.

Example: If the given number is 4, the output should be:
*
* *
* * *
* * * *

'''
n = int(input())
c =  1
while c <= n:
    print("* " * c)
    c = c + 1  
