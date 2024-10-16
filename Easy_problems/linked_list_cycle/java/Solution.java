package Easy_problems.linked_list_cycle.java;
import Easy_problems.utils.java.ListNode;


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

 class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode singleHopper = head;
        ListNode doubleHopper = head;

        while(true){
            if(!singleNullCheck(singleHopper)){
                singleHopper = singleHopper.next;
            }
            else break;
            if(!doubleNullCheck(doubleHopper)) doubleHopper = doubleHopper.next.next;
            else break;
            
            if (singleHopper == doubleHopper) return true;
        }
        return false;
    }

    private boolean singleNullCheck(ListNode n){
        return n == null;
    }

    private boolean doubleNullCheck(ListNode n){
        return singleNullCheck(n) || singleNullCheck(n.next);
    }
}
