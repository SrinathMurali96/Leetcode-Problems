#Best Time to Buy and Sell Stock II
#
#Example 1:
#Input: [7,1,5,3,6,4]
#Output: 7
#Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
#Example 2:
#
#Input: [1,2,3,4,5]
#Output: 4
#Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#             engaging multiple transactions at the same time. You must sell before buying again.
#             
ar = [7,6,4,3,1]
cur_min = ar[0]
max_val = ar[0]
total_profit = 0
for i in range(1,len(ar)):
    if  ar[i] > max_val :
        max_val = ar[i]
    else :
        if cur_min!=max_val:
            print(cur_min,max_val)
            total_profit =total_profit+ max_val- cur_min
        cur_min = ar[i]
        max_val = ar[i]
if cur_min!=max_val:      
    total_profit =total_profit+ max_val- cur_min
print(cur_min,max_val)
print("total_profit is ",total_profit)

