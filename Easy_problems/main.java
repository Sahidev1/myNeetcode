import reverse_linked_list.java.Solution;
import reverse_linked_list.java.Solution.ListNode;
class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] vals = {0,1,2,3};
        ListNode l = arrToListNode(vals, sol);
        listNodeIterator(l);
        l=sol.reverseList(l);
        System.out.println("reversed");
        listNodeIterator(l);

    }

    private static ListNode arrToListNode(int[] arr, Solution sol){
        ListNode root = sol.new ListNode(arr[0], null);
        ListNode curr = root;
        for(int i = 1; i < arr.length; i++){
            curr.next = sol.new ListNode(arr[i],null);
            curr = curr.next;
        }
        return root;
    }

    private static void listNodeIterator(ListNode root){
        while(root != null){
            System.out.println(root.val);
            root = root.next;
        }
    }
}