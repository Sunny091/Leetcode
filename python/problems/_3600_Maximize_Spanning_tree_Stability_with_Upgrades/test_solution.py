import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from solution import Solution


class TestSolution:
    def setup_method(self):
        self.sol = Solution()

    def test_example_1(self):
        # TODO: Add test case
        n = 3
        edges = [[0,1,2,1],[1,2,3,0]]
        k = 1
        assert self.sol.maxStability(n, edges, k) == 2

    def test_example_2(self):
        # TODO: Add test case
        n = 3
        edges = [[0,1,4,0],[1,2,3,0],[0,2,1,0]]
        k = 2
        assert self.sol.maxStability(n, edges, k) == 6
    
    def test_example_3(self):
        # TODO: Add test case
        n = 3
        edges = [[0,1,1,1],[1,2,1,1],[2,0,1,1]]
        k = 0
        assert self.sol.maxStability(n, edges, k) == -1
