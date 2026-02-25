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
        nums = [1,1,0,1]
        expected = 3
        assert self.sol.longestSubarray(nums) == expected

    def test_example_2(self):
        # TODO: Add test case
        nums = [0,1,1,1,0,1,1,0,1]
        expected = 5
        assert self.sol.longestSubarray(nums) == expected
    
    def test_example_3(self):
        # TODO: Add test case
        nums = [1,1,1]
        expected = 2
        assert self.sol.longestSubarray(nums) == expected

    def test_example_4(self):
        # TODO: Add test case
        nums = [0,0,0]
        expected = 0
        assert self.sol.longestSubarray(nums) == expected
