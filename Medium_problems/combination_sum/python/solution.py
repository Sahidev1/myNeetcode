class Solution:
    def csum(self, sum:int, built:list[int]):
        if sum == self.target:
            cpy = built.copy() #O(n)
            cpy.sort() #O(nlogn)
            cpy=tuple(cpy) # O(n)
                    
            if cpy not in self.combs: self.combs.add(cpy)
            
            return False
        elif sum > self.target: return False
        else:
            for i in range(len(self.nums)):
                s=sum+self.nums[i]
                built.append(i)
                r=self.csum(s, built);
                built.pop()
                if r is False: break
            
            return True
        
       
    
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        self.target:int = target
        self.combs:set[list[int]] = set()
        self.nums:list[int] = nums
        self.nums.sort()
        
        self.csum(0,[])
        
        res=[]
        for tup in self.combs:
            lst = []
            for e in list(tup):
                lst.append(self.nums[e])
            res.append(lst)
        
        return res
    

sol = Solution()

input=[2,5,6,9]
target=9

s=sol.combinationSum(input, target)
print(s)