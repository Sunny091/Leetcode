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
        nums1 = [1,2,3]
        nums2 = [2,4,6]
        expected = [[1,3],[4,6]]
        assert self.sol.findDifference(nums1, nums2) == expected

    def test_example_2(self):
        # TODO: Add test case
        nums1 = [1,2,3,3]
        nums2 = [1,1,2,2]
        expected = [[3],[]]
        assert self.sol.findDifference(nums1, nums2) == expected
    
    # def test_example_3(self):
    #     # TODO: Add test case
    #     pass
