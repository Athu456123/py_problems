s = input()
sum = 0

for i in s:
    if i == '{':
        sum = sum + 1
    elif i == '}':
        sum = sum - 1
    if sum < 0:
        break
if sum == 0:
    print("Matching")
else:
    print("Not Matching")