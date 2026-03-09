N = input()
check = int(N[2]) != 5 or int(N[0]) != 5 
if check and (int(N) > 300 and int(N) < 700):
    print("Valid Number")
else:
    print("Not a Valid Number")