
import java.lang.Math;
import java.util.Scanner;

class Solution {
    private boolean max_overflow = false;
    private boolean max_overflow_alert = false;
    private boolean min_overflow = false;
    private boolean min_overflow_alert = false;
    private static final int MAX = Integer.MAX_VALUE;
    private static final int MIN = Integer.MIN_VALUE;

    // O(1)
    private int kthDigit(int num, int k) {
        int res = num;
        for (int i = 1; i <= k; i++)
            res /= 10;

        return res % 10;
    }

    // O(1)
    private int pow10(int pow) {
        int res = 1;
        while (pow-- > 0) {
            res *= 10;
        }
        return res;
    }

    // O(1)
    private int digitCount(int num) {
        int count = 0;
        while (num != 0) {
            num /= 10;
            count++;
        }
        return count;
    }

    private int reverser(int x, int i, int digCnt) {
        if (i > digCnt)
            return 0;
        int kdig = kthDigit(x, digCnt - i);
        int pow = pow10(i - 1);

        int res = reverser(x, i + 1, digCnt);

        if (x >= 0) {
            if (i - 1 >= 9 && kdig == kthDigit(MAX, 9)) {
                this.max_overflow_alert = true;
            }
            if (i - 1 >= 9 && kdig > kthDigit(MAX, 9)) {
                this.max_overflow = true;
                return 0;
            }

            if (this.max_overflow_alert) {
                if (kdig > kthDigit(MAX, i - 1)) {
                    this.max_overflow = true;
                    return 0;
                }
                if (kdig < kthDigit(MAX, i - 1))
                    this.max_overflow_alert = false;
            }
        } else {
            if (i - 1 >= 9 && kdig == kthDigit(MIN, 9)) {
                this.min_overflow_alert = true;
            }
            if (i - 1 >= 9 && kdig < kthDigit(MIN, 9)) {
                this.min_overflow = true;
                return 0;
            }

            if (this.min_overflow_alert) {
                if (kdig < kthDigit(MIN, i - 1)) {
                    this.min_overflow = true;
                    return 0;
                }
                if (kdig > kthDigit(MIN, i - 1))
                    this.min_overflow_alert = false;
            }
        }

        return kdig*pow + res;
    }

    public int reverse(int x) {
        // int[] digits = new int[digitCount(x)];
        this.min_overflow=false;
        this.min_overflow_alert=false;
        this.max_overflow = false;
        this.max_overflow_alert = false;

        //System.out.println(digitCount(MAX));
        //System.out.println(digitCount(MIN));

        int res = reverser(x, 1, digitCount(x));
        return this.max_overflow || this.min_overflow ? 0 : res;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        // make interactive test with IO run in a loop
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("Enter an integer to reverse (or 0 to exit): ");
            int input = scanner.nextInt();
            if (input == 0)
                break;
            int reversed = sol.reverse(input);
            System.out.println("Reversed integer: " + reversed);
        }
        scanner.close();
    }
}
