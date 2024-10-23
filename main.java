import Easy_problems.balanced_binary_tree.java.Solution;
import utils.java.TreeNode;

class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();

        TreeNode tree = createRandomBalancedTree(new TreeNode(),1000000);

        long start = System.currentTimeMillis();
        System.out.println(sol.isBalanced(tree));
        long end = System.currentTimeMillis();
        System.out.println("Time: " + (end - start) + "ms");
    }

    private static TreeNode createRandomBalancedTree(TreeNode root,int nrNodes){
        if(nrNodes == 0){
            return null;
        }
        root = new TreeNode(0);
        root.left = createRandomBalancedTree(root.left,nrNodes/2);
        root.right = createRandomBalancedTree(root.right,nrNodes - nrNodes/2 - 1);
        return root;
    }
}