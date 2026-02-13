'''
Docstring for Day-40.Compare First & Last Letters
Question: Compare First & Last Letters
Write a program that reads a word and checks if the first letter and last letter of the word are not the same. The input will be a single line containing a string. The output should be a single line containing a boolean. True should be printed if the first letter and last letter of the word are not the same, otherwise False should be printed.

For example, if the given word is Python, the output should be True as the first letter P and the last letter n of the word are not the same.
'''
word = input()
compare = word[0] != word[-1]
result = compare
print(result)