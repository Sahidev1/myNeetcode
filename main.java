
import java.util.List;

import Medium_problems.Subsets.java.Solution; 

class Main {
    public static void main(String[] args) throws Exception {
        Solution sol = new Solution();
        int[] nums = {1,2,3};

        List<List<Integer>> res = sol.subsets(nums);

        System.out.println("starting with size: " + res.size());

        for (List<Integer> list : res) {
            System.out.print("[");
            for ( int i : list) {
                System.out.print(i + ",");
            }
            System.out.println("]");
        }

    }
}