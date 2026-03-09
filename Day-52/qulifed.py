M = int(input())
P = int(input())
check = M > 35 and P > 35
if check or M + P >= 100:
    print("Qualified")
else:
    print("Not Qualified")