5420. Final Prices With a Special Discount in a Shop

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discount_list = []
        for i in range(0,len(prices)-1):
            j = i+1
            condition = False
            while condition == False and j<len(prices):
                if prices[j] <= prices[i] and j>i:
                    discount_list.append(prices[i] - prices[j])
                    condition = True
                else:
                    j+=1
            if condition == False:
                discount_list.append(prices[i])
        discount_list.append(prices[len(prices)-1])
        return (discount_list)