'''Question: Percentage of Boys
Write a program that reads the percentage of girls in a class and prints the percentage of boys in the class. 
The total percentage of boys and girls in a class is 100.'''

girls_percentage = input()
girls_percentage = int(girls_percentage)

boys_percentage = 100 - girls_percentage
print(boys_percentage)