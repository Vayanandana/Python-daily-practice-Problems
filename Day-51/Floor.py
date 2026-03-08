'''
Write a program that reads a Room Number and checks if the Number in the given Room Number is less than 30.

The Room Numbers are in the format of R1, R35, etc.

Print Ground Floor if the Number is less than 30. Otherwise, print Not Ground Floor.'''
Room_Number = input()
Room_Number = int(Room_Number[1:])
if Room_Number < 30:
    print("Ground Floor")
else:
    print("Not Ground Floor")