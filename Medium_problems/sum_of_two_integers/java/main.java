import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class main {

    public static void main(String[] args) {
        BitSum summer = new BitSum();

        Scanner in = new Scanner(System.in);

        final String QUIT="quit";
        final String FORMATTER = "%08x";

        tests();

        String line = "";
        while(!line.equals(QUIT)){
            System.out.println("enter A: ");
            int a = in.nextInt();
            System.out.println("enter B: ");
            int b = in.nextInt();

            int res = summer.getSum(a, b);

            System.out.println(String.format(FORMATTER, a)+ " + " + String.format(FORMATTER,b) + " = " + String.format(FORMATTER, res));
            
            line = in.next();
        }


    }


    public static void tests(){
        BitSum summer = new BitSum();
        Map<int[], int[]> res = new HashMap<>();
        int[][] cases = {{0,0,0},{1,0,0},{1,1,0}, {0,0,1},{1,0,1},{1,1,1}};

        int[] restemp;
        for (int[] v : cases) {
            restemp = new int[2];
            restemp[0] = summer.bitSum(v[0],v[1], v[2], 0, 0x1);
            restemp[1] = summer.carryOut(v[0],v[1] , v[2], 0, 0x1);
            res.put(v, restemp);
        }

        String S = ", ";
        res.forEach((k,v) -> System.out.println(k[0] + S + k[1] + S + k[2] + "==> sum: " + v[0] + ", carryout: " + v[1] ));
    }


}