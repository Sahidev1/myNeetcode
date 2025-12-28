    
import random
import heapq



class Solution:

    #O(klogk) + O((N-k)logk) = O(Nlogk)
    def findKthLargest(self, nums: list[int], k: int) -> int:
        MinHeap = []
        
        i = 0
        
        #O(klogk)
        while len(MinHeap) < k:
            heapq.heappush(MinHeap, nums[i])
            i+=1
        #O((N-k)logK)    
        for j in range(i,len(nums)):
            if nums[j]>MinHeap[0]:
                heapq.heapreplace(MinHeap,nums[j]) #O(logK)


        return MinHeap[0]
    
    
sol=Solution()

input=[]
for i in range(10):
    input.append(random.randint(0,(100)))
print(input)
k=3
r=sol.findKthLargest(input,k)
input.sort(reverse=True)
s=""
for i in range(len(input)):
    if i == k-1:
        s+=f'[{input[i]}], '
    else:
        s+=f'{input[i]}, '
print(s)
print(r)