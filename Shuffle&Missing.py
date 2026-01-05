arr1 = list(map(int, input().split(',')))
arr2 = list(map(int, input().split(',')))
for i in arr1:
    if i not in arr2:
        print(i)
        break   
        