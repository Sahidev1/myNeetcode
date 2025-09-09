
import math


def bucketIt(map:dict, bucketCount:int, maxcount:int)->list[int]:
    k = bucketCount
    buckets = [[] for i in range(0,k)]
    M = maxcount + 1

    keys = map.keys()
    for elem in keys:
        buckets[math.floor((map[elem]*k)/M)].append(elem)

    return buckets




class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        map:dict[int,int] = {}

        maxCount = 0

        for elem in nums:
            if elem not in map:
                map[elem] = 1
            else:
                map[elem] +=1
            if map[elem] > maxCount: maxCount = map[elem]

        buckets = bucketIt( map, len(nums), maxCount)
        result = []
        buckIndex = len(nums) - 1
        
        while k > 0:
            if buckIndex < 0: break
            elif len(buckets[buckIndex]) == 0:
                buckIndex -= 1
                continue
            else:
                if (k >= len(buckets[buckIndex])):
                    for elem in buckets[buckIndex]: 
                        result.append(elem)
                        k -= 1
                else: 
                    buckets[buckIndex].sort()
                    while k > 0:
                        result.append(buckets[buckIndex].pop())
                        k -= 1
                buckIndex -= 1
                    
        return result
        

        

list=[2,2,3,5,7,7,2,5,6,7,5,5,9]

sol = Solution()
res=sol.topKFrequent(list, 3)        
print(res)