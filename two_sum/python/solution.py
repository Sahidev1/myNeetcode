from typing import List

# Difficulty easy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = i + 1
        arrLen = len(nums)
        while i < arrLen - 1:
            j = i + 1
            while j < arrLen:
                if nums[i] + nums[j] == target:
                    return [i,j]
                j += 1
            i += 1