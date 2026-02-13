'''
Docstring for Day-40.Validate Password
Question: Validate Password
Write a program to check if the given string is a valid password or not. A string is considered as a valid password if the number of characters present is greater than 7.

Input: The input will be a single line containing a word.

Output: The output should be True or False.

Explanation: For example, if the given input is "passwd", it has only 6 characters (less than 7). So the output should be False.
'''

word = input()
word = len(word)
validate = word > 7
print(validate)