A = int(input())
if (A % 5 == 0 and A % 7 == 0) or A < 7:
    print(A)
else:
    print(A % 5)
    print(A % 7)
