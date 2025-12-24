# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return f'[val: {self.val}]-->{self.next.__str__()}'

class Solution:
    def removeNthFromEnd(self, head , n: int):
        fast = head
        for i in range(0,n): fast = fast.next
    
        slow = head
        
        if fast == None:
            head = head.next
        else: 
            while fast.next != None:
                fast = fast.next
                slow = slow.next
            slow.next = slow.next.next
        
        return head
        
        
        
sol = Solution()

headl = [4]; n = 1

head = ListNode(headl[0])

curr = head
for i in range(1,len(headl)):
    curr.next = ListNode(headl[i])
    curr = curr.next

print(head)
res = sol.removeNthFromEnd(head,n)
print(res)