# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.recover_node(self.root)

    def recover_node(self, node):
        x = node.val
        if node.left is not None:
            node.left.val = (2*x) + 1
        
        if node.right is not None:
            node.right.val = (2*x) + 2

    def find(self, target: int) -> bool:
        # found = False
        q = deque()
        q.append(self.root)
        while q:
            curr_node = q.pop()
            if curr_node.val == target:
                return True

            self.recover_node(curr_node)
            if curr_node.left is not None and curr_node.left.val <= target:
                q.append(curr_node.left)
            
            if curr_node.right is not None and curr_node.right.val <= target:
                q.append(curr_node.right)
        
        return False




# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)