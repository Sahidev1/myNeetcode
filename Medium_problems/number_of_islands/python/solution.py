
from typing import List, Tuple



LAND="1";WATER="0"


class Solution:
    
    #O(1)
    def _get_visit_list(self, from_X, from_Y)->List[Tuple[int,int]]:
        lst=[]
        if from_X - 1 >= 0: lst.append((from_X - 1, from_Y))
        if from_X + 1 <= self.MAXROW: lst.append((from_X + 1, from_Y))
        if from_Y - 1 >= 0: lst.append(( from_X, from_Y - 1))
        if from_Y +1 <= self.MAXCOL: lst.append((from_X, from_Y + 1))
        return lst
    
    #O(size(island))
    def _explore_island(self, X:int, Y:int)->List[Tuple[int,int]]|None:
        if self.visited[X][Y]: return None
        if self.grid[X][Y] == WATER:
            return [(X,Y)]
        
        self.visited[X][Y] = True
        
        tovisit:List[Tuple[int,int]]=self._get_visit_list( X ,Y)
        waters=[]
        for coord in tovisit:
            ret = self._explore_island(coord[0], coord[1])
            if ret:
                waters+=ret
        
        return waters
        
    #O(m*n)
    def _search(self, X:int, Y:int):
        if self.visited[X][Y]: return
        
        if self.grid[X][Y] == LAND:
            ret=self._explore_island(X,Y)
            self.island_cnt+=1
            if ret:
                for x,y in ret:
                    self._search(x,y)
            return
                
            
            
        self.visited[X][Y]=True
        visitlist=self._get_visit_list(X, Y)
        for coord in visitlist:
            self._search(coord[0],coord[1])
            
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid=grid
        self.visitcount=0
        self.visited:List[List[bool]] = []
        self.island_cnt=0
        self.MAXROW=len(grid)-1;self.MAXCOL=len(grid[0])-1
        for row in grid:
            self.visited.append([False]*len(row))
        
        self._search(0,0)
        return self.island_cnt
        
        
grid=[["1","1","1","1","1","0","1","1","1","1"],
      ["1","0","1","0","1","1","1","1","1","1"],
      ["0","1","1","1","0","1","1","1","1","1"],
      ["1","1","0","1","1","0","0","0","0","1"],
      ["1","0","1","0","1","0","0","1","0","1"],
      ["1","0","0","1","1","1","0","1","0","0"],
      ["0","0","1","0","0","1","1","1","1","0"],
      ["1","0","1","1","1","0","0","1","1","1"],
      ["1","1","1","1","1","1","1","1","0","1"],
      ["1","0","1","1","1","1","1","1","1","0"]]


sol=Solution()

res=sol.numIslands(grid)
print(res)