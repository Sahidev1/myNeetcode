
public class BitSum {


    public int getSum(int a, int b) {
        final int BITCNT=32;
        int carry = 0;
        int sum = 0;
        int mask = 0x1;

        for(int i = 0; i < BITCNT; i++){
            sum |= bitSum(a, b, carry, i, mask);
            carry = carryOut(a, b, carry, i, mask);
            mask <<= 1;
        }


        return sum;
    }


    int bitSum(int a, int b, int carryin, int bitIndex, int mask){
        return (a&mask)^(b&mask)^(carryin<<bitIndex);
    }

    int carryOut(int a, int b, int carryin, int bitIndex, int mask){
        int A = a&mask;
        int B = b&mask;
        int C = carryin << bitIndex;
        int res = (A&B)|(B&C)|(A&C);

        return res >> bitIndex;
    }

}


