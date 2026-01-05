s = input()

sum = 0 
valley = 0
for i in range(len(s)):
    if s[i] == 'U':
        sum = sum +1
    elif s[i] == 'D':
        sum = sum - 1
    if sum == 0 and s[i] == 'U' :
        valley +=1
  

print(valley)