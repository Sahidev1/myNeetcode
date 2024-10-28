package Easy_problems.same_tree.java;

import utils.java.TreeNode;

//import arraydequeu
import java.util.ArrayDeque;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */

public class Solution {

    private void enQueue(ArrayDeque<TreeNode> queue, TreeNode t) {
        if (t != null)
            queue.add(t);
    }

    private TreeNode deQueue(ArrayDeque<TreeNode> queue) {
        return queue.pollFirst();
    }

    /*
     * worst case time complexity(is the same tree): O(n).
     * Mem complexity is O(n) due to queue structure.
     * 
     */
    public boolean isSameTree(TreeNode p, TreeNode q) {
        ArrayDeque<TreeNode> pQ = new ArrayDeque<>();
        ArrayDeque<TreeNode> qQ = new ArrayDeque<>();
        enQueue(pQ, p);
        enQueue(qQ, q);

        TreeNode pt, qt;
        while (true) {
            qt = deQueue(qQ);
            pt = deQueue(pQ);
            if (qt == null && pt == null)
                break;
            if (qt == null || pt == null)
                return false;
            if (qt.val != pt.val)
                return false;
            if (qt.left == null ^ pt.left == null) return false;
            enQueue(qQ, qt.left);
            enQueue(pQ, pt.left);
            if (qt.right == null ^ pt.right == null) return false;
            enQueue(qQ, qt.right);
            enQueue(pQ, pt.right);
        }
        return true;
    }
}
