# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return f'[val: {self.val}]-->{self.next.__str__()}'

class Solution:
    def removeNthFromEnd(self, head , n: int):
        curr = head
        nodecnt = 0
        
        #O(n)
        while curr != None:
            nodecnt += 1
            curr = curr.next
            
        target = nodecnt - n +1
        i=1
        curr = head
        prev = head
        
        #O(n)
        while i < target:
            prev = curr
            curr = curr.next
            i+=1
        
        if curr == prev:
            head = head.next
        else:
            prev.next = curr.next
        
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