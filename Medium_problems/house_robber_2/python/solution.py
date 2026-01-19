

from typing import List

UNVISITED=-1

class Solution:
    
        
      
    def robbery(self, houses:List[int], curr: int, stop:int):
        #print(houses)
        #print(curr, N_houses)
        if curr >= stop: return 
        if curr == stop - 1:
            self.memo[curr] = houses[curr%len(houses)]
            return
        
        #if rob this house:{}  
        if self.memo[curr + 1] == UNVISITED:
            self.robbery(houses, curr + 1,stop)
        self.memo[curr] = self.memo[curr + 1]
    
        if self.memo[curr+2] == UNVISITED:
            self.robbery(houses, curr + 2,stop)
        
        self.memo[curr] = max(self.memo[curr], houses[curr%len(houses)] + self.memo[curr + 2])
        
        
            

    def rob(self, nums: List[int]) -> int:
        memos=[[UNVISITED]*(len(nums))+[0,0,0],[UNVISITED]*(len(nums))+[0,0,0]]
        #print(memos)
        self.memo:list[int] = memos[0]
        self.robbery(nums, 0,len(nums))
        #print(memos)
        self.memo=memos[1]
        #print(nums)
        self.robbery(nums,1, len(nums)+1)
            
        print(memos)
        
        return max(memos[0][0],memos[1][1])
       

sol=Solution()
nums=[3,4,3]
print(sol.rob(nums))

    
