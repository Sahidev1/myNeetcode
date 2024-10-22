package Easy_problems.balanced_binary_tree.java;

import utils.java.TreeNode;

public class Solution {

    
    public boolean isBalanced(TreeNode root) {
        if(root == null) return true;
        if(abs(height(root.right) - height(root.left)) > 1) return false;
        return isBalanced(root.left) && isBalanced(root.right);
    }

    private int abs(int v){
        return v >= 0?v:-v;
    }

    private int height(TreeNode start){
        if(start == null) return 0;
        int lh = height(start.left) + 1;
        int rh = height(start.right) + 1;
        return lh > rh?lh:rh;
    }

}