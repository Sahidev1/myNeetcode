package Easy_problems.last_stone_height.java;

import java.util.Collections;
//import priority queue lib 
import java.util.PriorityQueue;

public class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        for (int stone : stones) {
            pq.add(stone);
        }

        int largest = 0;
        int second = 0;
        while(pq.size() > 1){
            largest = pq.remove();
            second = pq.remove();
            if (largest != second) {
                pq.add(largest - second);
            }
        }

        return pq.size() == 0?0:pq.peek();

    }
}
