class Solution(object):
    def maxProfit(self, prices):
        max = 0
        min = prices[0]

        for price in prices:
            if price < min:
                min = price

            profit = price - min

            if profit > max:
                max = profit

        return max

object = Solution()
print(object.maxProfit)