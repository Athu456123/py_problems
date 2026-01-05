stock = list(map(int,input().split(',')))
max_sum = 0 
n = len(stock)
for i in range(n-1):
    for j in range(i+1,n):
        add = stock[j] - stock[i]
        if add > max_sum:
            max_sum = add

print(max_sum)