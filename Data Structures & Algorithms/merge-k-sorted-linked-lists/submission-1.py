# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while True: 
            min_index = -1
            for i in range(len(lists)): 
                if not lists[i]: 
                    continue
                if min_index == -1 or lists[i].val < lists[min_index].val:
                    min_index = i
            if min_index == -1: 
                break
            else:
                cur.next = lists[min_index]
                cur = cur.next
                lists[min_index] = lists[min_index].next
        return dummy.next
        

        

        