

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
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

sol = Solution()
s="pwwwkew"

print(sol.lengthOfLongestSubstring(s)) # 4