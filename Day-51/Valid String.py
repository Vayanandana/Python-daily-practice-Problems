'''Write a program that reads a string S and checks if the length of S is between 2 and 7 or the first character of S is not equal to "a".

Print Valid String if the length of S is between 2 and 7 or the first character of S is not equal to "a". Otherwise, print Not a Valid String.

'''
s = input()
string = len(s)
check = string > 2 and string < 7
check2 = s[0] != "a"
if check or check2:
    print("Valid String")
else:
    print("Not a Valid String")