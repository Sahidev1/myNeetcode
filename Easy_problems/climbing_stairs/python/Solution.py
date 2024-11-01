class Solution:
    def climbStairs(self, n: int) -> int:
        self.mem:dict = {}
        return self.climb(n)


    def climb(self, n:int)->int:
        if n <= 3: return n
        remember = self.mem.get(n)
        if remember != None: return remember
        climb2 = self.climb(n - 2)
        climb1 = self.climb(n - 1)
        self.mem[n] = climb1 + climb2
        return climb1 + climb2