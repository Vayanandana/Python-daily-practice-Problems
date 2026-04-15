n = int(input())
val = ""
c = 0
for i in range(m,n+1):
    if i % 6 == 0:
        c = c + 1
        val = val + str(i) + (" ")
if c == 0:
    print("No Numbers Found")
else:
    print(val)
