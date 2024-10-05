package Easy_problems.reverse_bits.java;

class Solution {
    public int reverseBits(int n) {
        int B = 0x0;
        int maxI = 31;
        int C = maxI;
        int R = maxI - C;

        int extr = 0;
        while(C >= 0){
            B = (n & (0x1 << C)) == 0? B & ~(0x1 << R): B | (0x1<<R);
            C--;
            R = maxI - C;
        }
        return B;
    }
}
