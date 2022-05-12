# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        res = list3
        while list1 and list2:
            if list1.val <= list2.val:
                list3.next = ListNode(list1.val)
                list3 = list3.next
                list1 = list1.next
            else:
                list3.next = ListNode(list2.val)
                list3 = list3.next
                list2 = list2.next
        if list1:
            while list1:
                list3.next = ListNode(list1.val)
                list3 = list3.next
                list1 = list1.next
        if list2:
            while list2:
                list3.next = ListNode(list2.val)
                list3 = list3.next
                list2 = list2.next
                
        return res.next
                
        