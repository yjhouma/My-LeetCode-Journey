# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        resid = 0
        n = l1.val + l2.val + resid
        if n>=10:
            n -= 10
            resid += 1
    
        result_node = ListNode(val=n)
        nextNode = None

        while (l1.next is not None) or (l2.next is not None):
            if l1.next is not None:
                l1 = l1.next
                num1 = l1.val
            else:
                num1 = 0

            if l2.next is not None:
                l2 = l2.next
                num2 = l2.val
            else:
                num2 = 0
            
            sums = num1+num2+resid
            resid = max(0, resid-1)

            if sums >= 10:
                sums -= 10
                resid += 1
        
            if result_node.next is None:
                result_node.next = ListNode(val=sums)
                nextNode = result_node.next
            else:
                nextNode.next = ListNode(val=sums)
                nextNode = nextNode.next
        
        if resid >= 1:
            if nextNode is None:
                result_node.next = ListNode(val=1)
            else:
                nextNode.next = ListNode(val=1)
                nextNode = nextNode.next
        
        return result_node





        