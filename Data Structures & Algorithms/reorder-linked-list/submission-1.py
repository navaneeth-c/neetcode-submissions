# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return None

        slow, fast = head, head

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
        

        first = head
        second = slow.next
        slow.next = None

        # reverse second list
        prev, current = None, second 
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        second = prev
        while second: 
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2


            