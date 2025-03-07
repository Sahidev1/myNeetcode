

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        for v in nums:
            currSum = max(v, v + currSum)
            maxSum = max(maxSum, currSum)

        return maxSum
