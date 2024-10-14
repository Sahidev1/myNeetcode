class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxP:int = 0
        baseI:int = 0
        arrLen:int = len(prices)

        while baseI < arrLen - 1:
            nextI = baseI + 1
            while nextI < arrLen:
                currProf = prices[nextI] - prices[baseI]
                if currProf > maxP: maxP = currProf
                nextI += 1
            baseI += 1
        
        return maxP