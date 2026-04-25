n = int(input())
n2 = int(input())
if (n % 3 == 0 and n2 % 3 == 0) and n % 12 == 0 or n2 % 12 == 0:
    print("Pair")
else:
    print("Not a Pair")
