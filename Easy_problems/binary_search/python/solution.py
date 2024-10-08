
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        b = 0
        t = len(nums) - 1
        v = target
        m: int =  (b + t)//2

        while b < t: 
            if nums[m] == v: return m
            elif nums[m] < v: 
                b = m + 1
            else: 
                t = m - 1
            m = (b + t)//2
        
        if nums[m] == v: return m
        return -1 



sol = Solution()
print(sol.search([-1,0,3,5,9,12], 9)) # 4
print(sol.search([-1,0,3,5,9,12], 2)) # -1
print(sol.search([5], 5)) # 0