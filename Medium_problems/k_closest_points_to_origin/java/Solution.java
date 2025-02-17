package Medium_problems.k_closest_points_to_origin.java;

import java.util.Comparator;
import java.util.PriorityQueue;

public class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(points.length,
            new Comparator<int[]>() {
                @Override
                public int compare(int[] arg0, int[] arg1) {
                    int dist0 = euclidean(arg0);
                    int dist1 = euclidean(arg1);

                    return dist0 - dist1;
                }

                private int euclidean(int[] p){
                    return p[0]*p[0] + p[1]*p[1];
                }
            }
        );  

        for(int[] p: points){
            pq.add(p);
        }

        int[][] kth_closest = new int[k][2];
        
        while(--k >= 0){
            int[] removed = pq.poll();
            kth_closest[k][0] = removed[0]; kth_closest[k][1] = removed[1];
        }

        return kth_closest;
    }
}
