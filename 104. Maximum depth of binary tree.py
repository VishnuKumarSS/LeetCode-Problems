from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.depth = 0
        self.root = None

    def insert(self, val):
        new_node = TreeNode(val)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.val == temp.val:
                return False
            if new_node.val < temp.val:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     left = root.left
    #     right = root.right
    #     while left:
            
    #     while right:
    #         if root.left

my_tree = Solution()
my_tree.insert(5)
my_tree.insert(10)
my_tree.insert(15)
print(my_tree.root.val)
print(my_tree.root.right.val)
print(my_tree.root.right.right.val)