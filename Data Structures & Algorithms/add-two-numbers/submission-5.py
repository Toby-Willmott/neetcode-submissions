# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2: 
            print(l1, l2)
            if l1 == None: 
                a = 0
                b = l2.val
            elif l2 == None: 
                a = l1.val
                b = 0 
            else: 
                a = l1.val
                b = l2.val
            total = a + b + carry
            print(total)
            carry = total // 10
            print(carry)
            total = total % 10 
            print(total, "\n")
            curr.next = ListNode(total)
            curr = curr.next
            if l1: 
                l1 = l1.next 
            if l2: 
                l2 = l2.next
        if carry != 0: 
            curr.next = ListNode(carry)
            curr = curr.next
        return dummy.next
        