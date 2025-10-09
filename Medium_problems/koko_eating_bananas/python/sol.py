

'''
You are given an integer array piles where piles[i] is the number of bananas in the ith pile.
You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

'''

def pop_max(lst: list[int])->int:
    
    max_i = 0
    
    for i in range(len(lst)):
        if lst[i] > lst[max_i]: max_i = i
        
    return lst.pop(max_i)



class Solution:
    
    def max_val(self, piles: list[int]):
        mx = piles[0]
        
        for v in piles:
            mx = max(mx, v)
        
        return mx
        
    # O(h)
    def eat_speed_k(self, piles:list[int], k, h):
        curr_h = 0
        pile = piles[0]
        
        '''while curr_h < h:
            pile -= k
            if pile <= 0:
                i += 1
                if i < len(piles): pile = piles[i]
                else: break
            curr_h += 1
        '''
        
        #faster
        
        i = 0
        while i < len(piles):
            curr_h = curr_h +  (piles[i] // k)
            if piles[i] % k != 0: curr_h += 1
            if curr_h > h:
                break
            i += 1
        
        
        return (curr_h, i)        
        
            
            
            
    #O(log(maxval))
    def bin_search(self, piles:list[int], h, s):
        #lv = s//h 
        #if lv <= 0: lv = 1
        
        if s > h:
            lv = s//h
        else:
            lv = 1
        
        rv = self.max_val(piles)
      
        ##print(s,h,lv, rv)
        
        min_k=rv
    
        while(lv <= rv):
            k = (lv + rv) // 2
            res = self.eat_speed_k(piles, k, h)
            #print(f'(lv,rv):{(lv, rv)} ,(hours, maxindex): {res}, k:{k}, h:{h}')
            if res[1] < len(piles):
                lv = k + 1
            else:
                min_k = k
                rv = k - 1
            
                
        return min_k                
                
                
    
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        return self.bin_search(piles, h, sum(piles))
        
        
    
    
sol = Solution()

piles=[30,11,23,4,20]
h=6


#print(piles)

res = sol.minEatingSpeed(piles, h)
#print(res)

piles=[312884470]
h=968709470


#print(piles)

res = sol.minEatingSpeed(piles, h)
#print(res)

