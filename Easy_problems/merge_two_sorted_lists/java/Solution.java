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
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        return sort(list1, list2);    
    }

    private ListNode sort(ListNode a, ListNode b){
        if (a == null && b == null) return null;
        if (a == null || b == null){
            ListNode nonNull = a == null?b:a;
            return nonNull;
        }
        ListNode accum = null;
        if (a.val == b.val){
            accum = new ListNode(a.val, new ListNode(b.val));
            accum.next.next = sort( a.next, b.next);
        }
        if (a.val < b.val || a.val > b.val){
            ListNode lesser = a.val < b.val?a:b;
            ListNode larger = a.val < b.val?b:a;
            accum = new ListNode(lesser.val);
            accum.next = sort( lesser.next, larger);
        }
        return accum;
    }
}