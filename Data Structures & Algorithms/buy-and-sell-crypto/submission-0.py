class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        largest = 0
        buy = prices[0]
        sell = 0
        min = 0
        print(prices[1:])
        for index, price in enumerate(prices): 
            if index == 0: 
                continue
            sell = price
            print("sell", sell)
            if prices[index-1] < buy: 
                buy = prices[index-1]
                print("buy", buy)
            if sell - buy > largest: 
                largest = sell - buy
                print("largest", largest)
        return largest

            



        