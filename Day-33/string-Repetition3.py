string = input()
string_length = (len(string)) -2
result = string[0] + "*" * string_length + string[len(string)-1]
print(result)