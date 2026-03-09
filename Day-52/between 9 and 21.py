A = int(input())
B = int(input())
C = int(input())
check1 =  A > 9 and A < 21
check2 =  B > 9 and B < 21
check3 =  C > 9 and C < 21
if check1 or check2 or check3:
    print("True")
else:
    print("False")