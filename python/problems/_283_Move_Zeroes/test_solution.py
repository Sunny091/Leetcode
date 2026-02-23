import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from solution import Solution


class TestSolution:
    def setup_method(self):
        self.sol = Solution()

    def test_example_1(self):
        nums = [0, 1, 0, 3, 12]
        self.sol.moveZeroes(nums)
        assert nums == [1, 3, 12, 0, 0]

    def test_example_2(self):
        nums = [0]
        self.sol.moveZeroes(nums)
        assert nums == [0]
    
    # def test_example_3(self):
    #     # TODO: Add test case
    #     pass
