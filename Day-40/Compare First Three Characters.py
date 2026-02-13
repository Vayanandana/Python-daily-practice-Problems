'''
Question: Compare First Three Characters
Write a program to check if the first three characters in the two given strings are the same.

Input:

The first line of input will be a string.
The second line of input will be a string.
Output:

Print "True" if the the first three characters in the two given strings are the same.
In all other cases print "False".
Example:

When the given words are "Apple" and "Application", first three characters in both the strings are the same ("App")
When the given words are "Android" and "Application", the first three characters in both the strings are different ("And" != "App")
'''
string_1 = input()
string_2 = input()
check = string_1[0:3] == string_2[0:3]
result = check
print(result)