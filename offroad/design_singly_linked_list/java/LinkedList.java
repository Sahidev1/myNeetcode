import java.util.ArrayList;

public class LinkedList {
    class Node {
        int value;
        Node next;

        public Node(int val) {
            this.value = val;
        }

        public Node(Node next, int val) {
            this.next = next;
            this.value = val;
        }
    }
    private static final int OUT_OF_BOUNDS_CODE = -1;


    private Node head;
    private Node tail;
    int elemCount;

    public LinkedList() {
        this.head = null;
        this.tail = this.head;
        this.elemCount = 0;
    }

    private void nullHeadInit(int val) {
        this.head = new Node(val);
        this.tail = this.head;
    }

    public int get(int index) {
        if (index >= this.elemCount) return OUT_OF_BOUNDS_CODE;
        if (index == this.elemCount - 1) return this.tail.value;
        Node curr = this.head;
        int i = 0;

        while(i++ < index) {
            curr = curr.next;
        }
        
        return curr.value;
    }

    public void insertHead(int val) {
        if (this.head == null) {
            nullHeadInit(val);
        } else {
            Node n = new Node(this.head, val);
            this.head = n;
        }
        this.elemCount++;
    }

    public void insertTail(int val) {
        if (this.head == null) {
            nullHeadInit(val);
        } else {
            Node n = new Node(val);
            tail.next = n;
            tail = tail.next;
        }
        this.elemCount++;
    }

    public boolean remove(int index) {
        if (index >= this.elemCount) return false;
        else if (index == 0){
            this.head = this.head.next;
            if (this.head == null){
                this.tail = this.head;
            }
        }
        else{
            int i = 0;
            Node curr = this.head;

            while(i++ < index - 1){
                curr = curr.next;
            }

            curr.next = curr.next.next;
            if (curr.next == null){
                this.tail = curr;
            }
        }
        this.elemCount--;
        return true;
    }

    public ArrayList<Integer> getValues() {
        ArrayList<Integer> list = new ArrayList<>();
        int i = 0;
        Node curr = this.head;

        while (i++ < this.elemCount){
            list.add(curr.value);
            curr = curr.next;
        }

        return list;
    }
}
