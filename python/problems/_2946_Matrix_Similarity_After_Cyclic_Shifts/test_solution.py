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
        mat = [[1,2,3],[4,5,6],[7,8,9]]
        k = 4
        assert self.sol.areSimilar(mat, k) == False

    def test_example_2(self):
        # TODO: Add test case
        mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]]
        k = 2
        assert self.sol.areSimilar(mat, k) == True

    def test_example_3(self):
        # TODO: Add test case
        mat = [[2,2],[2,2]]
        k = 3
        assert self.sol.areSimilar(mat, k) == True
