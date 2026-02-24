from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def calculate(self, node: Optional[TreeNode], current_sum: int) -> int:
        if not node:
            return 0
        
        current_sum = (current_sum << 1) | node.val
        
        if not node.left and not node.right:
            return current_sum
        
        return self.calculate(node.left, current_sum) + self.calculate(node.right, current_sum)

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        """
        LeetCode 1022. Sum of Root To Leaf Binary Numbers

        TODO: Implement your solution here
        """
        return self.calculate(root, 0)
