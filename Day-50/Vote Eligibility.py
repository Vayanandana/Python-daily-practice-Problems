'''In this coding question, you need to write a program that reads the age of a person and checks if the person is eligible to vote. 
If the age of the person is greater than or equal to 18, the person is eligible to vote, and you should print "Eligible". Otherwise, print "Not Eligible"'''
age = int(input())
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")