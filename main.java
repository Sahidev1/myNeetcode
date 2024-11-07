import Easy_problems.kth_largest_element_in_a_Stream.java.KthLargest;
import Easy_problems.kth_largest_element_in_a_Stream.java.KthLargest.HeapTree;
import Easy_problems.kth_largest_element_in_a_Stream.java.KthLargest.ORDERING;

class Main {
    public static void main(String[] args) throws Exception {

       /* uSE THIS TEST CASE: 
        * ["KthLargest","add","add","add","add","add"]
            [[3,[5,-1]],[2],[1],[-1],[3],[4]]
        */
        int[] arr = {5, -1};
        KthLargest kthLargest = new KthLargest(3, arr);
        HeapTree ht = kthLargest.getHeapTree();
        ht.insert(2);
        ht.insert(1);
        ht.printHeap();
        for (int i = 0; i < 4; i++) {
            System.out.println(ht.remove());
            ht.printHeap();
        }
        /*System.out.println(kthLargest.add(2));   // returns 2
        System.out.println(kthLargest.add(1));   // returns 1
        kthLargest.getHeapTree().printHeap();
        System.out.println(kthLargest.getHeapTree().kthOrderedVal(3));
        /*System.out.println(kthLargest.add(-1));  // returns 1
        System.out.println(kthLargest.add(3));   // returns 2
        System.out.println(kthLargest.add(4));   // returns 3
*/
    }
}