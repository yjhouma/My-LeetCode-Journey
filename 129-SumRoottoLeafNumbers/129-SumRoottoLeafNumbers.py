# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        stack = []
        stack.append((root, str(root.val)))
        numbers = []
        while stack:
            node, num = stack.pop()
            if node.left is None and node.right is None:
                numbers.append(int(num))
        
            if node.left is not None:
                new_number = num + str(node.left.val)
                stack.append((node.left, new_number))

            if node.right is not None:
                new_number = num + str(node.right.val)
                stack.append((node.right, new_number))
        
        # print(numbers)
        return sum(numbers)




