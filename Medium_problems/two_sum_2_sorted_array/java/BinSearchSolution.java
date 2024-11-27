package Medium_problems.two_sum_2_sorted_array.java;



class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] ret = new int[2];
        
        int search = -1;
        for(int i = 0; i < numbers.length; i++){
            search = binSearch(numbers, i, target);
            if(search != -1){
                ret[0] = i + 1;
                ret[1] = search + 1;
                return ret;
            }
        }

        return ret;
    }

    private int binSearch(int[] numbers, int leftIndex, int target){
        int b = leftIndex + 1;
        int t = numbers.length - 1;
        int lVal = numbers[leftIndex];
        int m = (b + t) / 2;
        int s;

        while(m <= t && m >= 0 && b <= t){
            s = numbers[m] + lVal;
            if(s == target) return m;
            else if (s < target) b = m + 1;
            else t = m - 1;

            m = (b + t) / 2;
        }

        return -1;
    }
}
