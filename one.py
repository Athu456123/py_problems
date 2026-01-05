'''
day = int(input())

if day % 5 == 0:
    print("pinky finger")
if day % 5 == 1:
    print("thumb finger")
if day % 5 == 2:
    print("index finger")
if day % 5 == 3:
    print("middle finger")
if day % 5 == 4:
    print("ring finger")
'''
arr = list(map(int, input().split()))
n = int(input())
unique = set()
for i in range(len(arr)):
    for j in range(len(arr)):
        if abs(arr[i] - arr[j]) == n:
            pair = tuple(sorted((arr[i], arr[j])))
            unique.add(pair)


print(len(unique))

