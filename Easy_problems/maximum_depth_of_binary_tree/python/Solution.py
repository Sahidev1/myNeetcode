
from typing import Optional
from utils.python.TreeNode import TreeNode





class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #USING DFS ALGO
        if root is None: return 0

        lval = self.maxDepth(root.left) + 1
        rval = self.maxDepth(root.right) + 1

        return lval if lval > rval else rval