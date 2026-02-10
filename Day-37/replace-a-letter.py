'''
Docstring for Day-37.replace-a-letter
The program is designed to perform a specific string manipulation task based on the following requirements:

Read a word W.
Read an index I.
Read a letter C.
Replace the letter in W at the position given by I with the letter C.
Logical Approach:

Read Inputs:
Read the word W as a string.
Read the index I as an integer.
Read the letter C as a string.

Replace the Letter at Index I with C:
Slice the string W into two parts:
The part before the index I.
The part after the index I.
Concatenate the first part, the letter C, and the second part.

Output:
Print the new word obtained after the replacement.

Example for Clarity:

Given the word W as Prime, index I as 3, and letter C as z:
The substring before the 3rd index (0-based) is Pri.
The letter at the 3rd index is m which needs to be replaced with z.
The substring after the 3rd index is e.
After replacement, the word becomes Prize
'''
word = input()
index = int(input())
letter = input()
change = word[0:index] + letter + word[index+1:]
result = change 
print(result)
