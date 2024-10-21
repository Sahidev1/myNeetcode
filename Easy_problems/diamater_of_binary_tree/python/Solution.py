from typing import Optional
from utils.python.TreeNode import TreeNode 

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #DFS
        [larger, maxFound] = self._DFS(root)
        return maxFound

    def _DFS(self ,root: Optional[TreeNode])-> tuple[int,int]:
        
        if root is None: return [0, 0]
  
        [lval, lmax] = self._DFS(root.left)
        [rval, rmax] = self._DFS(root.right)
        largestMax = lmax if lmax > rmax else rmax
        currMax = lval + rval 
        retMax = currMax if currMax > largestMax else largestMax 
        larger = lval if lval > rval else rval

        return [larger + 1, retMax]
        

        

