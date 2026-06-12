class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largest = 0
        buy = prices[0]
        sell = 0
        min = 0
        for index, price in enumerate(prices): 
            if index == 0: 
                continue
            sell = price
            if prices[index-1] < buy: 
                buy = prices[index-1]
            if sell - buy > largest: 
                largest = sell - buy
        return largest

            



        