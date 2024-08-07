class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 팔거나 사거나, 안사거나
        bought = False
        profit = 0
        for i in range(len(prices) - 1):
            if not bought:
                if prices[i+1] > prices[i]:
                    bought = True
                    bPrice = prices[i]
            else:
                if prices[i+1] <= prices[i]:
                    bought = False
                    profit += prices[i]-bPrice
        if bought:
            profit += prices[-1]-bPrice
        return profit
