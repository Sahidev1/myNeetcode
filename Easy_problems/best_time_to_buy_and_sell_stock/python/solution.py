class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxP:int = 0
        arrLen:int = len(prices)
        lPtr:int = 0
        rPtr:int = lPtr + 1
        lowest = prices[lPtr]

        while rPtr < arrLen:
            if prices[lPtr] < lowest: lowest = prices[lPtr]
            currP = prices[rPtr] - lowest
            if currP > maxP: maxP = currP
            lPtr = rPtr
            rPtr += 1

        
        return maxP