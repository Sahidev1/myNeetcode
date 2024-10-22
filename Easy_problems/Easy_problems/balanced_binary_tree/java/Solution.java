package Easy_problems.balanced_binary_tree.java;

import Easy_problems.utils.java.TreeNode;


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

 class Solution {
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
