
import java.util.List;

import Medium_problems.k_closest_points_to_origin.java.Solution;

class Main {


    public static void main(String[] args) throws Exception {
        int[][] points = {{0,2},{2,0}, {2,2}};
        int k = 2;

        pointArrayPrinter(points);

        Solution sol = new Solution();

        int[][] kth_closest = sol.kClosest(points, k);
        System.out.println("kth:");
        pointArrayPrinter(kth_closest);
    }

    private static void pointArrayPrinter(int[][] points){
        for (int[] p: points){
            System.out.println("[" + p[0] + "," + p[1] + "]");
        }
    }
}