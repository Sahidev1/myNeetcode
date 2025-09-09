

    

import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        map:dict[int, int] = {}

        for i in range(len(nums)):
            elem = nums[i]
            if elem not in map:
                map[elem] = 1
            else:
                map[elem] += 1
        
        data = [(-val, key) for key, val in map.items()]

        heapq.heapify(data)
        result = []

        for i in range(0,k):
            result.append(heapq.heappop(data)[1])


        return result
        

list=[2,2,3,5,7,7,2,5,6,7,5,5,9]

sol = Solution()
sol.topKFrequent(list, 3)        