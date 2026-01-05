n = int(input())
arr = input().split()
string_dct ={}

for word in arr :
    x = tuple(sorted(word))
    print(x)

    if x in string_dct:
        string_dct[x] = string_dct.append(word)
    else :
        string_dct[x] = [word]

for i in string_dct.values():
    print(' '.join(i))






