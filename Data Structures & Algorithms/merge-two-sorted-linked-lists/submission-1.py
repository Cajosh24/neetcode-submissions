# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        if list1.val <= list2.val:
            new_head = list1
        else:
            new_head = list2

        current1 = list1
        current2 = list2
        prev = None

        while current1 and current2:

            if current1.val <= current2.val:
                print("connecting 1 to 2 |||", current1.val,current2.val )
                if prev is None:
                    prev = current1
                else:
                    prev.next = current1
                    prev = current1

                current1 = current1.next
            else:
                print("connecting 2 to 1 |||", current2.val,current1.val )
                if prev is None:
                    prev = current2
                else:
                    prev.next = current2
                    prev = current2

                current2 = current2.next
            

        if current2:
            prev.next = current2
        else:
            prev.next = current1

        return new_head
    

                
        