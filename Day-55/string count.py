string = input()
c = 0
for i in string:
    if (i == "a") or (i == "e") or (i == "i") or (i == "o") or (i == "u"):
        c = c + 1
if c > 2:
    print("String has more than two vowels")
else:
    print("String doesn't have more than two vowels")
