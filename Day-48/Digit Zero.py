num = input()
check1 = int(num[0]) == 0 
check2 = int(num[1]) == 0 
check3 = int(num[2]) == 0
compare = (check1 or check2 ) or  check3
print(compare)