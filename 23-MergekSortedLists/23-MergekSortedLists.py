# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def all_list_is_none(self, lists):
        for l in lists:
            if l is not None:
                return False
        
        return True



    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        if self.all_list_is_none(lists):
            return None

        # Case if all node have elements
        minimum = inf
        min_idx = None
        for i,l in enumerate(lists):
            if l is not None and l.val < minimum:
                minimum=l.val
                min_idx = i

        lists[min_idx] = lists[min_idx].next
        head = ListNode(minimum)
        tail = None

        while not self.all_list_is_none(lists):
            minimum = inf
            min_idx = None
            for i,l in enumerate(lists):
                if l is not None and l.val < minimum:
                    minimum=l.val
                    min_idx = i
            
            lists[min_idx] = lists[min_idx].next
            if tail is None:
                head.next = ListNode(minimum)
                tail = head.next
            else:
                tail.next = ListNode(minimum)
                tail = tail.next
        
        return head


        