package Easy_problems.sub_tree_of_another_tree.java;

import utils.java.TreeNode;

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
    private final int HASH_VAL = 0;
    private final int HEIGHT = 1;

    private int getHashFactor(int height){
        return 1 << ((height) % 31); 
    }

  

    private int hashFn(TreeNode t, int lHash, int rHash, int height){
        if (t == null) return 0;
        return ((3*lHash + 5*rHash) + t.val*getHashFactor(height));
    }

    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        int srHash = subRootHash(subRoot)[HASH_VAL];
        int[] res = traverse(root, srHash);
        return res[HASH_VAL] == srHash;
    }

    private int[] traverse(TreeNode root, int subRootHash){
        if (root == null){
            return new int[]{0, 0};
        }
        int[] l = traverse(root.left, subRootHash);
        if(l[HASH_VAL] == subRootHash) return l;
        int [] r = traverse(root.right, subRootHash);
        if(r[HASH_VAL] == subRootHash) return r;

        int height = Math.max(l[HEIGHT], r[HEIGHT]) + 1;
        int currHash = hashFn(root, l[HASH_VAL], r[HASH_VAL],height);

        r[HASH_VAL] = currHash;
        r[HEIGHT] = height;
        return r;
    }

    private int[] subRootHash(TreeNode sr){
        if (sr == null) return new int[]{0,0};
        int[] l = subRootHash(sr.left);
        int[] r = subRootHash(sr.right);
        
        int height = Math.max(l[HEIGHT], r[HEIGHT]) + 1;
        int hash = hashFn(sr, l[HASH_VAL], r[HASH_VAL], height);
        r[HASH_VAL] = hash;
        r[HEIGHT] = height;
        return r;
    }
}
