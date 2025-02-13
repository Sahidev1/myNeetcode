package Medium_problems.Subsets.java;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    List<List<Integer>> subsets = new ArrayList<>();

    public List<List<Integer>> subsets(int[] nums) {
        procedure(nums, 0, new ArrayList<>());
        return subsets;
    }

    private void procedure(int[] nums, int curr, List<Integer> list){
        if (curr >= nums.length){
            this.subsets.add(list);
            return;
        }

        procedure(nums, curr + 1, list);

        List<Integer> listcpy = new ArrayList<>(list);
        listcpy.add(nums[curr]);
        procedure(nums, curr + 1, listcpy);
    }
}
