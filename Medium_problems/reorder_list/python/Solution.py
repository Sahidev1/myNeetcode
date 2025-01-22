
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def arrayToList(arr):
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return head

def ListToArray(head):
    arr = []
    current = head
    while current != None:
        arr.append(current.val)
        current = current.next

    return arr

printList = lambda head: print(ListToArray(head))

class Solution:
    def getMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s, f = head, head # slow, fast
        size = 0
        prevs = head
        while f != None and f.next != None:
            prevs = s
            s = s.next
            f = f.next.next
            size+=2
        if f is not None: size+=1
        
        if size % 2 == 0: s = prevs

        return s

    def createSecondList(self, mid)-> tuple[Optional[ListNode], Optional[ListNode]]:
        if mid.next is None:
            return None
        else: 
            nxt = mid.next
            mid.next = None
            return nxt

    def reverseList(self, head: Optional[ListNode])-> Optional[ListNode]:
        prev, curr = None, head
        while curr is not None:
            saveNext = curr.next
            curr.next = prev
            prev = curr
            curr = saveNext

        return prev
        

    def mergeLists(self, base: Optional[ListNode], appending: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = base, appending

        while l1 is not None and l2 is not None:
            l1next = l1.next
            l2next = l2.next
            l1.next = l2
            l2.next = l1next
            l1, l2 = l1next, l2next

    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.getMiddle(head)
        l2 = self.createSecondList(mid)
        l2=self.reverseList(l2)
        self.mergeLists(head, l2)


def test(arr: list[int]):
    head = arrayToList(arr)
    printList(head)
    sol = Solution()
    sol.reorderList(head)
    printList(head)

testCases: list[list[int]] = [
    range(0,1),
    range(0,2),
    range(0,3),
    range(0,4),
    range(0,5),
    range(0,6),
]

for test_case in testCases:
    print("Test case nr: ", testCases.index(test_case))
    test(test_case)
    print("\n\n")

