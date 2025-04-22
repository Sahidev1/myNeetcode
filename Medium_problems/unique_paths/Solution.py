import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #starting at (0,0) moving to (m-1, n-1) --> must make m-1 down moves and n - 1 right moves
        #think of it as possible unique combination of m-1 R's and n-1 D's with no repetition and in order.
        #total elements is N_D + N_R --> (N_D + N_R)!. 
        #There is going to be overlapping combinations where we could switch around the R's and D's and the sequence still looks the
        #To ignore this we divide by N_D! and N_R! so final formula is: (N_D + N_R)!/(N_D! * N_R!)

        f = self.f
        nR = n - 1
        nD = m - 1
        return math.floor(f(nR + nD) / (f(nR)*f(nD)))
    
    def f(self,n:int):
        return math.factorial(n)
    

sol = Solution()
m=3
n=6

res = sol.uniquePaths(m,n)
print(res)