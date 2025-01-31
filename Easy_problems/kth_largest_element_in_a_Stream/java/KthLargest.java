package Easy_problems.kth_largest_element_in_a_Stream.java;




public class KthLargest {
    public enum ORDERING {
        MIN,
        MAX
    }

    public static class HeapTree{
        private ORDERING order;
        private Integer[] arr;
        private int maxD;
        private int treeSize;
        private int lastFree;

        public HeapTree(ORDERING ord){
            this.order = ord;
            this.treeSize = 2<<3;
            this.lastFree = 1;
            this.maxD = 4;
            generateTree();
        }

        public HeapTree(ORDERING ord, int[] initArr){
            this.order = ord;
            int initLen = initArr.length;
            this.lastFree = 1;
            int treeSize = 2<<3;
            int maxD = 4;
            while(treeSize < initLen) {
                treeSize <<= 1;
                maxD++;
            }
            this.maxD = maxD;
            this.treeSize = treeSize;
            generateTree();

            for (int i : initArr) {
                this.insert(i);
            }
        }

        public void insert(int v){
            if(this.lastFree >= arr.length) enlargeTreeArray();
            this.arr[this.lastFree++] = v;
            bottom_swim_heapify();
        }

        public Integer peek(){
            return this.arr[1];
        }

        public Integer remove(){
            Integer remVal = this.arr[1];
            
            this.arr[1] = this.arr[lastFree - 1];
            this.arr[lastFree - 1] = null;
            this.lastFree--;
            top_sink_heapify();
            return remVal;
        }

        public int[] heapSort(){
            int[] sorted = new int[this.lastFree - 1];
            int i = 0;
            Integer rem;
            while(this.lastFree > 1){
                rem = this.remove();
                if (rem != null) sorted[i++] = rem;
            }
            return sorted;
        }


        public int getTreeDepth(){
            return this.maxD;
        }

        public int getSize(){
            return this.lastFree - 1;
        }

        public void printHeap(){
            int depth = 1;
            System.out.print("|");
            for (int i = 1; i < arr.length; i++){
                System.out.print(this.arr[i] + " ");
                if (i == Math.pow(2, depth) - 1){
                    System.out.print("|");
                    System.out.println();
                    System.out.print("|");
                    depth++;
                }
            }
            System.out.println();
        }

        private void bottom_swim_heapify(){
            swim_heapify(this.lastFree - 1);
        }

        private void swim_heapify(int curr){
            if (curr == 1) return;
            int parent = curr / 2;
            if(arr[parent] == null){
                swap(curr, parent);
                swim_heapify(parent);
            }
            else if(this.order == ORDERING.MIN){
                if (arr[parent] > arr[curr]) {
                    swap(curr, parent);
                    swim_heapify(parent);
                } 
            } else {
                if(arr[parent] < arr[curr]){
                    swap(curr, parent);
                    swim_heapify(parent);
                } 
            }
        }

        private void top_sink_heapify(){
            sink_heapify(1);
        }

        private void sink_heapify(int curr){
            if ((2*curr + 1) > this.lastFree) return;
            Integer lchild = arr[2*curr];
            Integer rchild = arr[2*curr + 1];
            if (lchild == null && rchild == null) return;
            if(this.order == ORDERING.MIN){
                int smallestIndex = curr;         
                if (lchild == null || rchild == null) {
                    smallestIndex = lchild == null?2*curr + 1:2*curr;
                } else {
                    smallestIndex = lchild < rchild?2*curr:2*curr + 1;
                }
                if (arr[smallestIndex] < arr[curr]){
                    swap(smallestIndex, curr);
                    sink_heapify(smallestIndex);
                } else return;
            } else {
                int largestIndex = curr;
                if (lchild == null || rchild == null) {
                    largestIndex = lchild == null?2*curr + 1:2*curr;
                } else {
                    largestIndex = lchild > rchild?2*curr:2*curr + 1;
                }
                if (arr[largestIndex] > arr[curr]){
                    swap(curr, largestIndex);
                    sink_heapify(largestIndex);
                } else return;
            }
        }

        private void swap(int i, int j){
            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
        }        

        private void enlargeTreeArray(){
            this.treeSize <<= 1;
            this.maxD += 1;
            Integer[] newArr = new Integer[this.treeSize];
            System.arraycopy(this.arr, 1, newArr, 1, this.arr.length - 1); 
            this.arr = newArr;

        }

        private void generateTree(){
            this.arr = new Integer[this.treeSize];
        }

    }

    private int k;
    private HeapTree minPQ;

    public KthLargest(int k, int[] nums)  {
        this.k = k;
        this.minPQ = new HeapTree(ORDERING.MIN);
        for (int i : nums) {
            this.add(i);   
        }
    }
    
    public int add(int val)  {
        int size = this.minPQ.getSize();
        Integer rootVal = this.minPQ.peek();
        if (rootVal == null || size < this.k){
            this.minPQ.insert(val);
        } 
        else {
            if (val > rootVal){
                this.minPQ.remove();
                this.minPQ.insert(val);
            }
        }
        return this.minPQ.peek();
    }

    public HeapTree getHeapTree(){
        return this.minPQ;
    }
}
