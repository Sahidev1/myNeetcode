
import TreeNode

class Solution:
    
    
    def visitNode(self,t:TreeNode, depth:int, nestlst:list[list[int]]):
        if t == None: return
        
        if len(nestlst) == depth: nestlst.append([])
        
        nestlst[depth].append(t.val)
        
        self.visitNode(t.left, depth+1, nestlst)
        self.visitNode(t.right, depth+1, nestlst)
        
    
    def levelOrder(self, root:TreeNode):
        depth = 0
        nstlst = []
        self.visitNode(root, depth, nstlst)
        return nstlst
    
    
root = []

t = TreeNode.build_tree_from_list(root)

sol = Solution()
res=sol.levelOrder(t)
print(res)