package Easy_problems.counting_bits.java;

class Solution {
    public int[] countBits(int n) {
        int[] arr = new int[n + 1];
        for (int i = 0; i < n + 1; i++){
            arr[i] = bitCount(i);
        }
        return arr;
    }

    private int bitCount(int n){
        int count = 0;
        int bitChecks = 32;
        for(int i = 0; i < bitChecks; i++){
            count += (n>>i)&(0x1);
        }
        return count;
    } 
}
