
ROW=0
COL=1


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        self.M = len(matrix) - 1
        self.Matrix = matrix

        start=0
        end = self.M 

        while start < end:
            startRow = start
            startCol = start

            while startCol < end:
                starting=[startRow, startCol]
                self.spiral(starting, [startRow, startCol], None, 0)
                startCol += 1

            
            start += 1
            end -= 1

        return
    
    def spiral(self, start:tuple[int], curr:tuple[int], prev:int, loops:int):
        currV = self.Matrix[curr[ROW]][curr[COL]]
        #print(str(curr) + ", " + str(prev) + ", " + str(currV))
        
        if loops > 0 and curr == start:
            self.Matrix[curr[ROW]][curr[COL]] = prev
            return
        
        self.spiral(start, self.transform(curr[ROW], curr[COL]), currV, loops + 1)
        if prev != None : self.Matrix[curr[ROW]][curr[COL]] = prev



    def transform(self,ROW:int, COL:int):
        return [COL, self.M - ROW]


def printMatrix(matrix: list[list[int]]):
    print("[")
    for row in matrix:
        print("    "+str(row) + ",")
    print("]")

sol = Solution()

test = [[1,2],[3,4]]
printMatrix(test)

sol.rotate(test)
printMatrix(test)
