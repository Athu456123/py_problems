#1.	An org. has arranged for an investor meetup so that the startup companies can come and
#  grab the max amount of investment possible. All investors seated in sequential order.
#  Every investor has their banking amounts visible each startup participating can get 
# as many investment are possible (min 2 investors, max total no of investor)
#  Help the startups gather as many investors as possible so that they have the max investment.

offer= list(map(int,input().split()))
#sum = 0
max_sum = 0
n = len(offer)
'''
for i in range(0,n-1):
    sum = offer[i]
    for j in range(i+1,n):
        sum = sum + offer[j]                     # NOT OPTIMISED 
        if sum >= 0 and sum > max_sum:
            max_sum = sum
    
print(max_sum)
'''
temp_sum =0
sum = offer[0] + offer[1]
for i in range(1,n):
    if sum > max_sum:
        max_sum = sum
    if sum >0 :
        sum = sum + offer[i+1]
    else:
        sum = offer[i] + offer[i+1]
        


