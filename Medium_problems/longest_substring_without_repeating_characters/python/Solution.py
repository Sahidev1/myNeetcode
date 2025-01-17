

import time


class Solution:
    #complexity is actually approximately O(n²)
    def lengthOfLongestSubstringUnoptimized(self, s: str) -> int:
        bag = set()
        i = 0
        clist = list(s)
        maxW = 0
        while(i < len(clist)):
            j = i
            while j < len(clist) and clist[j] not in bag: 
                bag.add(clist[j])
                j += 1
            
            bagsize = len(bag)
            if bagsize > maxW: maxW = bagsize
            bag.clear()
            i += 1

        return maxW

    #optimized solution 
    def lengthOfLongestSubstring(self, s: str) -> int:
        bag = set()
        b = 0 
        t = 0
        clist = s
        wmax = 0

        while t < len(clist):
            while t < len(clist) and clist[t] not in bag:
                bag.add(clist[t])
                t += 1
                
            wmax = max(t - b, wmax)                
            bag.discard(clist[b])
            b += 1
        
        return wmax



sol = Solution()

s="pwwkew"

start_time = time.time_ns()
print(sol.lengthOfLongestSubstringUnoptimized(s)) # 4
print("Time elapsed: ", time.time_ns() - start_time)

start_time = time.time_ns()
print(sol.lengthOfLongestSubstring(s)) # 4
print("Time elapsed: ", time.time_ns() - start_time)
