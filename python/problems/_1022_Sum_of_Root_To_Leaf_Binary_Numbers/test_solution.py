import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from solution import Solution, TreeNode
from collections import deque


def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


class TestSolution:
    def setup_method(self):
        self.sol = Solution()

    def test_example_1(self):
        root = build_tree([1,0,1,0,1,0,1])
        assert self.sol.sumRootToLeaf(root) == 22

    def test_example_2(self):
        root = build_tree([0])
        assert self.sol.sumRootToLeaf(root) == 0
    
    # def test_example_3(self):
    #     # TODO: Add test case
    #     pass
