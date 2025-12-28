class Solution:
    
    def subSum(self, base:int, sum:int, lst:list[int]):
        if sum == self.target:
            self.combs.append(lst.copy())
            return False
        elif sum > self.target: return False 
        else:
            for i in range(base, len(self.nums)):
                lst.append(self.nums[i])
                r=self.subSum(i, sum + self.nums[i], lst)
                lst.pop()
                if not r: break

        return True
        
    
   
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        self.nums = nums
        nums.sort()
        self.target = target
        self.combs:list[list[int]]=[]
        self.subSum(0,0,[])
        return self.combs
    

sol = Solution()

input=[2,5,6,9]
target=9

s=sol.combinationSum(input, target)
print(s)