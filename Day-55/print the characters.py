'''Write a program that reads a string and prints each character of the given string on a new line.

Input
The input will be a single line containing a string.

Output
The output should be N lines, with each line containing a string that is one of the characters of the given string. Here, N is the length of the given string.

Explanation
For example, if the given string is shine,

The length of the given string is 5.
Each character of the string should be printed on a new line.'''

string = input()
string_len = len(string)
c = 0
while c < string_len:
    print(string[c])
    c = c + 1