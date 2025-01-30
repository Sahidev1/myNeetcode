class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        xorSum = len(nums)
        i = 0
        for e in nums:
            xorSum = xorSum ^ (e^i)
            i += 1
        
        return xorSum 
    


sol = Solution()

print(sol.missingNumber([3,0,1])) # 2