
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        costLen = len(cost)
        self.memo:list[int] = [None]*costLen
        start0Cost = self.__traverse(cost, 0, costLen)
        start1Cost = self.__traverse(cost, 1, costLen)
        return self.__min2(start0Cost, start1Cost)


    def __traverse(self, cost: list[int], currI:int, maxI:int) -> int: 
        if currI >= maxI: return 0
        memCheck = self.memo[currI]
        if memCheck != None: return memCheck
        step1Cost = self.__traverse(cost, currI+1, maxI)
        step2Cost = self.__traverse(cost, currI+2, maxI)
        minCost = self.__min2(step1Cost, step2Cost) + cost[currI]
        self.memo[currI] = minCost
        return minCost
    
    def __min2(self, a:int, b:int)->int:
        return a if a < b else b