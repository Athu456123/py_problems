n = int(input())
num = list(map(int,input().split()))
sort = sorted(num)
triplets = set()
for i in range(0,n):
    for j in range(0,n):
        for k in range(0,n):
            if i != j and  i!= k and j != k:
                if sort[i] + sort[j] + sort[k] == 0:
                    triple = tuple(sorted((sort[i], sort[j], sort[k])))
                    triplets.add(triple)
print(triplets)
 