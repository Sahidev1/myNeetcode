import Easy_problems.kth_largest_element_in_a_Stream.java.KthLargest;
import Easy_problems.kth_largest_element_in_a_Stream.java.KthLargest.HeapTree;
import Easy_problems.kth_largest_element_in_a_Stream.java.KthLargest.ORDERING;

class Main {
    public static void main(String[] args) throws Exception {

        KthLargest sol = new KthLargest(3, new int[]{1000,-1000});

        System.out.println(sol.add(0));
        // generate integer array of size 1000 with random values
        /*int[] arr = new int[100];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (int) ((Math.random()-0.5) * 1000);
        }

        HeapTree ht = new HeapTree(ORDERING.MAX, arr);
        ht.printHeap();
        ht.insert(3);
        ht.insert(1);
        int k = 1 + (int) (Math.random() * 100);
        int kth = ht.kthOrderedVal(k);
        ht.printHeap();
        System.out.println("kth: " + kth);
        System.out.println("k: " + k);
        int[] sorted = ht.heapSort();
        for (int i = 0; i < sorted.length; i++) {
            if (i == k){
                System.out.print("[" + sorted[i] + "], ");
            } else {
                System.out.print(sorted[i] + ", ");
            }
        }*/
    }
}