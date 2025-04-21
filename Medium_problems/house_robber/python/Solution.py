
UNVISITED=-1
SKIPPED=0
ROBBED=1

class Solution:
    def rob(self, nums: list[int]) -> int:
        self.history: list[list[int]] = [[UNVISITED, UNVISITED] for i in range(len(nums))]

        sum = self.visit(0, nums, 0)

        return sum
    
    def visit(self, house: int, nums:list[int], sum:int):
        if house < 0 or house >= len(nums): return sum
       
        

        #skip it
        skipSum=0
        if self.history[house][SKIPPED] != UNVISITED:
            skipSum = sum + self.history[house][SKIPPED]
        else:
            skipSum = self.visit(house + 1, nums, sum)
            self.history[house][SKIPPED] = skipSum

        #rob it
        robSum=0
        if self.history[house][ROBBED] != UNVISITED:
            robSum = sum + self.history[house][ROBBED]
        else:
            robSum = self.visit(house + 2, nums, sum + nums[house])
            self.history[house][ROBBED] = robSum


        
        return max(robSum, skipSum)

    


sol = Solution()
nums=[1,2,1,1]


sum=sol.rob(nums)
print(sum)