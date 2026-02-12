'''
Docstring for Day-39.Greater than or Equal to
Question: Greater than or Equal to
Write a program that reads two numbers A and B and checks if A is greater than or equal to B. Print the result as shown in the sample output.

Input
The first line of input contains a float.
The second line of input contains a float.

Output
The output should be a single line containing a string as shown in the sample output.

Explanation
For example, if the given numbers are A = 4.3 and B = 3.2,

A is greater than or equal to B: True. (4.3 is greater than or equal to 3.2)
Add the string "A >= B is " before True.
The output should be A >= B is True.
'''
A = float(input())
B = float(input())
check = A >= B 
result = check 
print("A >= B is " +  str(result))