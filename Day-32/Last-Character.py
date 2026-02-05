'''
Write a program which prints the last character of a given word.

Input: The input will be a single line containing a word.

Output: The output should be a single line containing the last character of the given word.

Explanation: For example, if the given input word is "January", your code should print the last character "y".
'''
word = input()
word_length = len(word)
last_index  = word_length - 1
last_character = word[last_index]
result = last_character
print(result)