from collections import Counter
word = input()
c1 = Counter(word)
odd = 0

for i in c1:
    if c1[i] % 2 == 1:
        odd +=1
if odd == 1:
    print("True")
else:
    print("False")
    
