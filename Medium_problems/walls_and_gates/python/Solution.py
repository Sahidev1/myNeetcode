
CHEST= 0
WATER=-1
LAND=(2**31) - 1
INF=LAND

class Solution:
    # Complexity worst case: O(C*M*N), where C is number of chests
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        self.grid = grid
        self.M = len(grid)
        self.N = len(grid[0])
       
        self.visitMatrix:list[list[int]] = []
        for i in range(self.M):
            self.visitMatrix.append([0]*self.N)
        self.visitID = 0

        #print(self.visitMatrix)

        chests = self.getChests()
        #print("chests:")
        #print(chests)
        for (i,j) in chests:
            self.travelFromChest(i,j)


        return None
    
    def __readcell(self, i, j):
        s = ''
        cell = self.grid[i][j]
        if cell == CHEST: s="chest"
        elif cell == WATER: s="water"
        elif cell == INF: s="inf"
        else: s=f'land: {cell}'

        return s

    #worst case complexity: O(M*N)
    def travelFromChest(self, i, j):
        chestEdges:list[tuple[int]] = self.getEdges(i,j)
        self.visitID += 1
        initDist = 0

        ##print(f'edges to {(i,j)}:')
        ##print(chestEdges)
        for (a, b) in chestEdges:
            self.traverse(a,b, initDist + 1)

        ##print(self.visitMatrix)


    def traverse(self, i, j, dist):
        #print(self.visitMatrix)
        #print(f'\t traversing {(i,j)},cell: {self.__readcell(i,j)}')

        if self.grid[i][j] <= 0:
            return

        
        if self.visitMatrix[i][j] == self.visitID and self.grid[i][j] < dist: 
            return
  

        self.grid[i][j] = min(self.grid[i][j], dist) 
        self.visitMatrix[i][j] = self.visitID
        #print(f'visited: {(i,j)}')
      
        

        edges = self.getEdges(i,j)
        ##print(f'edges to {(i,j)}')
        ##print(edges)
        for (a,b) in edges:
            self.traverse(a,b,dist + 1)


    
    # retuns the edges of a cell
    #COMPLEXITY: O(1)
    def getEdges(self, i, j)->list[tuple[int]]:
        edges = []

        if j - 1 >= 0: edges.append((i, j - 1))
        if j + 1 < self.N: edges.append((i, j + 1))
        if i - 1 >= 0: edges.append((i - 1, j))
        if i + 1 < self.M: edges.append((i + 1, j))
        return edges
    
    #complexity: O(M*N)
    def getChests(self):
        chests = []

        for i in range(self.M):
            for j in range(self.N):
                if self.grid[i][j] == CHEST: chests.append((i,j))

        return chests
    

sol = Solution()

input = [[2147483647,2147483647,2147483647],[2147483647,-1,2147483647],[0,2147483647,2147483647]]





sol.islandsAndTreasure(input)

print(sol.grid)
##print(sol.visitMatrix)
