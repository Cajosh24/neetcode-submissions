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

        print(size,n)
        
        if size == 1:
            head = None
            return head
        elif size == n:
            head = head.next
            return head

        index = 1
        node = head
        while index < (size - n):
            node = node.next
            index += 1
        
        temp = node.next
        node.next = temp.next
        temp = None

        return head

    
            
        