a = int(input())
b = int(input())
check = a <= 1000 and b <= 1000
if check or b >= 500:
    print("Pair")
else:
    print("Not a Pair")