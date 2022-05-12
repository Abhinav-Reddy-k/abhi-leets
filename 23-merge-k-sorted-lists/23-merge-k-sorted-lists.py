# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = [(n.val,i,n) for i,n in enumerate(lists) if n]
        res = node = ListNode()
        heapq.heapify(h)
        
        while h:
            val,i,n = heapq.heappop(h)
            node.next = ListNode(val)
            node=node.next
            if n.next:
                heapq.heappush(h,(n.next.val,i,n.next))
        
        return res.next
            
            
        
        