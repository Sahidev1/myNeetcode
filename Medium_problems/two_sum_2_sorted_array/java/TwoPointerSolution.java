package Medium_problems.two_sum_2_sorted_array.java;

public class TwoPointerSolution {
    public int[] twoSum(int[] numbers, int target) {
        int lptr = 0;
        int rptr = numbers.length - 1;

        int s;
        while(lptr < rptr){
            s = numbers[lptr] + numbers[rptr];
            if (s == target) return new int[]{lptr + 1, rptr + 1};
            if(s > target) rptr--;
            else lptr++;
        }

        return new int[2];
    }    
}
