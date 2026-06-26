# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = [] 
        temp = head
        while temp: 
            nodes.append(temp)
            temp = temp.next
        num = len(nodes) - n
        
        dummy = ListNode()
        curr = dummy
        index = 0

        while index <= num: 
            if index == num:
                curr.next = head.next
                if index == len(nodes) -1: 
                    break
                else: 
                    head = head.next.next
                    curr = curr.next
            else:
                curr.next = head
                head = head.next
                curr = curr.next
            index += 1
        return dummy.next