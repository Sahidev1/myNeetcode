package Easy_problems.balanced_binary_tree.java;


import utils.java.TreeNode;

public class Solution {
    private static final int HEIGHT = 0;
    private static final int ISBALANCED = 1;

    public boolean isBalanced(TreeNode root) {
        int[] res = traverse(root);
        return balanceCheck(res);
    }

    private int[] traverse(TreeNode root){
        if (root == null) return new int[]{0,1};
        int[] ldata, rdata;
        ldata = traverse(root.left);
        if (!balanceCheck(ldata)) return ldata;
        rdata = traverse(root.right);
        if (!balanceCheck(rdata)) return rdata;

        int[] larger = ldata[HEIGHT] >= rdata[HEIGHT]?ldata:rdata;

        if (abs(ldata[HEIGHT] - rdata[HEIGHT]) > 1) {
            larger[ISBALANCED] = 0;
            return larger;
        }

        larger[HEIGHT] += 1;
        return larger;
    }

    private boolean balanceCheck(int[] data){
        return data[ISBALANCED] == 1;
    }

    private int abs(int v){
        return v >= 0?v:-v;
    }

}