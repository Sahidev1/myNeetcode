package Easy_problems.happy_number.java;

import java.util.Set;

//Diffuculty: Easy
class Solution {
    private final static int MAX = 1000; // if initial n is 999
    private boolean[] history = new boolean[MAX + 1];

    public boolean isHappy(int n){
        while(true){
            if (n == 1) return true;
            else if (history[n]) return false;
            history[n] = true;
            n = squareSumDigits(n);
        }
    }

    private int squareSumDigits(int n){
        int squareSum = 0;
        int currDig = 0;
        while(n > 0){
            currDig = n % 10;
            squareSum += currDig*currDig;
            n = n/10;
        }
        return squareSum;
    }
    

}
