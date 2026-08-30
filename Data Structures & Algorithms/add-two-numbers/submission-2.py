# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        node3 = head
        node1 = l1
        node2 = l2

        value1 = None
        value2 = None
        carry = 0
        
        while node1 or node2:
            #adding values
            if node1:
                value1 = node1.val
            else:
                value1 = 0
            
            if node2:
                value2 = node2.val
            else:
                value2 = 0
            
            num = value1 + value2 + carry
            
            if num >= 10:
                num = num - 10
                carry = 1
            else:
                carry = 0

            node3.val = num

            #increment nodes
            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next

            if node1 or node2:
                node3.next = ListNode(0)
                node3 = node3.next
            elif carry:
                node3.next = ListNode(carry)


        return head



        