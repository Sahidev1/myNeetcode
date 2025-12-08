


class Solution:    

        
    def find_longest_consecutive(self, s, k):
        strset=set(s)
        max_wsize=0
        
        #print(strset)
        
        for c in strset:
            l=0; r=l
            misses=0
            #print(f'C:{c}')
            while r < len(s):
                if s[r] == c: r+=1
                elif misses < k:
                    r+=1
                    misses+=1
                else:
                    max_wsize=max(max_wsize, r - l)
                    #print(misses)
                    #print(f'{s[0:l]}|{s[l:r]}|{s[r:len(s)]}')
                    if s[l] != c: misses -= 1

                    l+=1
            #print(f'{s[0:l]}|{s[l:r]}|{s[r:len(s)]}')
            max_wsize=max(max_wsize, r - l)
            
        return max_wsize
                    
                    
            
            
                        
                 
            
            
                
            
                
            
            
    #worst case: O(n^2 * u)
    def characterReplacement(self, s: str, k: int) -> int:
        return self.find_longest_consecutive(s,k)
    
        
    
    

sol = Solution()
s="XAXXAAAXAAAAA"
k=2
print(s)
r=sol.characterReplacement(s,k)
print(r)