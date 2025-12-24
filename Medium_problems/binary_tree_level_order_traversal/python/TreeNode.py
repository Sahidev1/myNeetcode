class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
    
        

    
         


def build_tree_from_list(lst, index=0):
    if index >= len(lst) or lst[index] is None:
        return None

    node = TreeNode(lst[index])
    node.left = build_tree_from_list(lst, 2 * index + 1)
    node.right = build_tree_from_list(lst, 2 * index + 2)
    return node
        
def treeNode_to_list_proc(t:TreeNode, lst:list[list[any]], lvl=0):
    if t == None: return
    if len(lst) == lvl: lst.append([])
    
    lst[lvl].append(t.val)
    
    treeNode_to_list_proc(t.left, lst, lvl + 1)
    treeNode_to_list_proc(t.right, lst, lvl + 1)
    
def treeNode_to_list(t:TreeNode):
    lst=[]
    treeNode_to_list_proc(t,lst)
    
    retlst=[]
    for subl in lst:
        retlst+=subl
        
    return retlst
    
    
    
    
        
    
    