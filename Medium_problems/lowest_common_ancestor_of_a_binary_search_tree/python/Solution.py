class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def arrayToTree(arr: list[int]) -> TreeNode:
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        current = queue.pop(0)
        if arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i+=1
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i+=1

    return root


class Solution:

    #complexity worst cases:
    # time: O(2*h + h) = O(h)
    # space: O(2*h + 2*h) = O(h), size of path stacks and call stack max size for recursive calls
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        pathstack_p:list[TreeNode] = []
        pathstack_q:list[TreeNode] = []
        self.getPathStack(root, p, pathstack_p)
        self.getPathStack(root, q, pathstack_q)


        #loop time-complexity worst case: O(h)
        lcm = None
        while (len(pathstack_p) > 0 and len(pathstack_q) > 0) and (pathstack_p[-1].val == pathstack_q[-1].val):
            lcm = pathstack_q[-1]
            pathstack_q.pop()
            pathstack_p.pop()
        
        return lcm
    
    #complexity worst cases
    # time: O(h), where h is height of tree
    # space: O(h), where h is height of tree
    def getPathStack(self, root: TreeNode, n: TreeNode, stack: list) -> None:
        if root == None: return
        
        stack.insert(0, root)
        
        if root.val == n.val:
            return
        elif (root.val > n.val):
            return self.getPathStack(root.left, n, stack)
        else:
            return self.getPathStack(root.right, n, stack)
        


sol = Solution()
arr = [5,3,8,1,4,7,9,None,2]
p = TreeNode(3)
q = TreeNode(8)
root = arrayToTree(arr)
lcm = sol.lowestCommonAncestor(root, p, q)
print(lcm.val)
