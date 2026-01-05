arr = list(map(int,input().split(',')))
n = int(input())
arr.sort()
'''
for i in range(len(arr)):
    for j in range(len(arr)):
        for k in range(len(arr)):
            sum = arr[i]+arr[j]+arr[k]  #BRUTE FORCE
            if sum == n:
                f += 1
            else:
                continue
if f>0:
    print("True")
else:
    print("False")
'''
                    #NEW CODE

'''
for i in range(len(arr)):
    left,right = i,len(arr) - 1
    while left <= right:
        sum = arr[i]+arr[left]+arr[right]  #BETTER OPTIMISED
        if sum < n:
            left +=1
        elif sum > n:
            right -= 1
        else:
            print("True")
            exit(0)
print("False")
'''

