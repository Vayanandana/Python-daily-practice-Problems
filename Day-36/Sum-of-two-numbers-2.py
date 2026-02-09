'''Question: Sum of two numbers - 2
Write a program that reads two numbers and prints the sum of two numbers in the given format.

Input
The first line of input contains a float.
The second line of input contains a float.

Output
The output should be a single line containing a string in the format shown in the sample output.'''

first_number = input()
second_number = input()

first_number = float(first_number)
second_number = float(second_number)

result = first_number + second_number

print("Sum: " + str(result))