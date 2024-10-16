package Easy_problems.invert_binary_tree.java;
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
    public TreeNode invertTree(TreeNode root) {
        return traverse(root);
    }

    private TreeNode traverse(TreeNode root){
        if(root == null) return null;
  
        TreeNode l = traverse(root.left);
        TreeNode r = traverse(root.right);
        root.left = r;
        root.right = l;

        return root;
    }
}
