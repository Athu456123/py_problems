nums = list(map(int,input().split(',')))
target = int(input())
start = 0
end = len(nums)
for i in range(end-1):
     for j in range(i+1,end):
        if nums[i] + nums[j] == target:
            print(f"[{nums[i]},{nums[j]}]")
            break