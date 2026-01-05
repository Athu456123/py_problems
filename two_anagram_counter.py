from collections import Counter
str1 = input()
str2 = input()
c1 = Counter(str1)
c2 = Counter(str2)
if c1 == c2:
    print("Anagram")
else:
    print("Not Anagram")
