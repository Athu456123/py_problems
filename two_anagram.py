str1 = input()
str2 = input()
str1_dct = {}
str2_dct ={}
for i in str1:
    if i in str1_dct:
        str1_dct[i] += 1  
    else:
        str1_dct[i] = 1

for i in str2:
    if i in str2_dct:
        str2_dct[i] += 1
    else:
        str2_dct[i] = 1

if str1_dct == str2_dct:
    print("Anagram")
else:
    print("Not Anagram")
