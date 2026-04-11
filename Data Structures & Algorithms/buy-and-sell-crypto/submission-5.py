class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l =0
        # r =1
        # profit = 0
        # while(r<len(prices)):
        #     if(prices[l]>prices[r]):
        #         l = r
        #     else:
        #         profit = max(profit, prices[r]-prices[l])
        #     r+=1
        # return profit

        buy = 0 
        sell = 1
        prof = 0
        while sell < len(prices):
            if prices[sell] > prices[buy]:
                prof = max(prof,prices[sell] - prices[buy])
            elif prices[sell] <= prices[buy]:
                buy = sell
            sell+=1
        return prof
        


        