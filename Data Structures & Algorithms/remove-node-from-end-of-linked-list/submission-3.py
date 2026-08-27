# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        node = head

        while node:
            size += 1
            node = node.next
        
        if size == 1:
            head = None
            return head
        elif size == n:
            head = head.next
            return head


        index = 1
        temp = ListNode(0,head)

        while index <= (size - n):
            temp = temp.next
            index += 1
        
        temp.next = temp.next.next

        return head

    
            
        