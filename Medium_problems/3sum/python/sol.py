



class Solution:
    def ranged2Sum(self, nums: list[int], res: list[list[int]], start_i:int, seeked_sum:int):
        lp = start_i
        rp = len(nums) - 1
        prev_lp = -1
        prev_rp = -1
        
        
        while lp < rp:
            if prev_lp > -1 and nums[lp] == nums[prev_lp]: 
                prev_lp = lp
                lp += 1
                continue
            
            while rp > lp:
                if prev_rp > -1 and nums[rp] == nums[prev_rp]:
                    prev_rp = rp
                    rp -= 1
                    continue
                
                s = nums[lp] + nums[rp]
                
                if s < seeked_sum:
                    break
                elif s > seeked_sum:
                    prev_rp = rp
                    rp -= 1
                else: 
                    res.append([-s ,nums[lp], nums[rp]])
                    break
                
            prev_lp = lp; lp += 1
            rp = len(nums) - 1; prev_rp = -1
             
            
                

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res: list[list[int]] = []
        
        curr = 0
        prev = -1
        size = len(nums)
        
        while curr < size:
            if prev > -1 and nums[curr] == nums[prev]: 
                prev = curr
                curr += 1
                continue
            
            c = -(nums[curr])
            self.ranged2Sum(nums, res,curr + 1, c)
            
            
            prev = curr; curr += 1
            
        return res
        
        
                    
                    
#sorted [-4,-1,-1,0,1,2]                    
nums = [-1,0,1,2,-1,-4]

sol = Solution()
res = sol.threeSum(nums)

print(res)




                
            