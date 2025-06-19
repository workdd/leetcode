class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        total_money = 0
        earned_money = 0
        
        for idx, price in enumerate(prices):
            if idx == 0:
                buy = price

            if buy < price:
                sell_money = price - buy
                total_money += sell_money
                buy = price
            else:
                buy = price
        return total_money
