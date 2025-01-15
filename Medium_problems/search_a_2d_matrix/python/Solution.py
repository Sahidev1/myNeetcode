

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        b = 0; t = len(matrix) - 1; rmax = len(matrix[0]) - 1

        while b <= t:
            m = (b+t)//2 
            first = matrix[m][0]; last = matrix[m][rmax]

            if target < first:
                t = m - 1
            elif target > last:
                b = m + 1
            else:
                return self.binSearchRow(matrix, m, target)

        return False            




    def binSearchRow(self, matrix: list[list[int]], row: int, target:int) -> bool:
        b = 0; t = len(matrix[row]) - 1

        while b <= t:
            m = (b + t)//2   
            val = matrix[row][m]
            if target < val:
                t = m - 1
            elif target > val:
                b = m + 1
            else: 
                return True
        
        return False



sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 16
print(sol.searchMatrix(matrix, target)) # True
target = 13
print(sol.searchMatrix(matrix, target)) # False
target = 3
print(sol.searchMatrix(matrix, target)) # True