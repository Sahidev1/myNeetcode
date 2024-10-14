package reverse_linked_list.java;


public class Solution {
    public class ListNode {
        public int val;
        public ListNode next;
        public ListNode() {}    ListNode(int val) { this.val = val; }
        public ListNode(int val, ListNode next) { this.val = val; this.next = next; }
      }

    public ListNode reverseList(ListNode head) {
        ListNode curr = head;
        ListNode saveNext;
        ListNode newNext = null;

        while(true){
            if(curr == null){
                head = newNext;
                break;
            }
            saveNext = curr.next;

            curr.next = newNext;
            newNext = curr;
            curr = saveNext;
        }

        return head;
    }

    
}
