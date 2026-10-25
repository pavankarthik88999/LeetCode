class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        i=0
        j=1
        n=len(prices)
        profit=0
        while j<n:
            if prices[i]<prices[j]:
                temp=prices[j]-prices[i]
                profit=max(temp,profit)
            else:
                i=j
            j=j+1

             
        return profit
        