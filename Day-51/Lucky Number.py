a = int(input())
b = int(input())
check1 = (a == 6 and b == 6)
check2 = (a + b) == 6
check3 = (a - b) == 6 
check4 = (b - a) == 6
if (check1 or check2) or (check3 or check4):
    print("Lucky")
else:
    print("Not Lucky")