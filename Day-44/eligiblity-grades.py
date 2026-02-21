maths =int(input())
physics = int(input())
chemistry = int(input())
Sum = maths + physics + chemistry
check = (maths >= 70 ) and (physics >= 60) and (chemistry >= 60)
compare = Sum >= 180 or check
print(compare)