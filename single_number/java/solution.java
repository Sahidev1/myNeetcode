class Solution {
    public int singleNumber(int[] nums) {
        int xored = xorAll(nums);
        return xored;
    }

    private int xorAll(int[] nums){
        int xored = nums[0];
        for(int i = 1; i < nums.length; i++){
            xored ^= nums[i];
        }
        return xored;
    }
}
