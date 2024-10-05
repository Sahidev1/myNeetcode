package contains_duplicate.java;

import java.util.HashSet;
import java.util.Set;

public class Solution {
    private Set<Integer> history = new HashSet<>();

    public boolean hasDuplicate(int[] nums) {
        for (int i : nums) {
            if (history.contains(i)) return true;
            history.add(i);
        }
        return false;
    }


}
