
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def generateLL(aar: list[int]) -> Optional[ListNode]:
    head = ListNode(aar[0])
    current = head
    for i in range(1, len(aar)):
        current.next = ListNode(aar[i])
        current = current.next
    return head

def printLL(head: Optional[ListNode]):
    while head != None:
        print(head.val)
        head = head.next


class Solution:
    def getLLSize(self, head: Optional[ListNode]) -> int:
        size = 0
        while head != None:
            size += 1
            head = head.next
        return size

    def moveSteps(self, start: Optional[ListNode], steps:int):
        while steps > 0:
            start = start.next
            steps -= 1

        return start
    


    def reorderList(self, head: Optional[ListNode]) -> None:
        nSize:int = self.getLLSize(head)
        steps = nSize - 1
        f = head

        print(f'List size: {nSize}, steps: {steps}')

        while steps > 0:
            n = f.next
            last = self.moveSteps(f, steps)
            print(f'f: {f.val}, last: {last.val}, n: {n.val}')
            f.next = last 
            last.next = n
            f = n
            steps -= 2
        
        f.next = None


llist = generateLL([1,2,3,4,5,6])
#printLL(llist)
sol = Solution()
sol.reorderList(llist)
printLL(llist)