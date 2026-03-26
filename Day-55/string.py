string = input()
string_len = len(string)
res_word =''
for i in range(1,string_len+1):
    res_word = res_word + string[-i]
print(res_word)
