class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur = 0
        earned_money = 0
        for idx, price in enumerate(prices):
            if idx == 0:
                cur = price
                continue
            if price < cur:
                cur = price
            else:
                cur_money = price - cur
                if cur_money > earned_money:
                    earned_money = cur_money
        return earned_money
