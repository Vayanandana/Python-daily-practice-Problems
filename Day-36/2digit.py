n = input()
convert_n = int(n)
if convert_n % int(n[0]) == 0 and convert_n % int(n[1]) == 0:
    number = convert_n
    print(number * 2)
else:
    number = convert_n
    print(number)
