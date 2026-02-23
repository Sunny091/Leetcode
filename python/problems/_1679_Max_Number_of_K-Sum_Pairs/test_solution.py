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
        nums = [1, 2, 3, 4]
        k = 5
        assert self.sol.maxOperations(nums, k) == 2

    def test_example_2(self):
        # TODO: Add test case
        nums = [3, 1, 3, 4, 3]
        k = 6
        assert self.sol.maxOperations(nums, k) == 1
    
    # def test_example_3(self):
    #     # TODO: Add test case
    #     pass
