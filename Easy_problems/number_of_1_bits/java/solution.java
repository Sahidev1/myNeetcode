package Easy_problems.number_of_1_bits.java;
class Solution {
    public int hammingWeight(int n) {
        return bitCount(n);
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