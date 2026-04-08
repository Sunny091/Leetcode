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
        nums = [1,1,1]
        queries = [[0,2,1,4]]
        expected = 4
        assert self.sol.xorAfterQueries(nums, queries) == expected



    def test_example_2(self):
        # TODO: Add test case
         nums = [2,3,1,5,4]
         queries = [[1,4,2,3],[0,2,1,2]]
         expected = 31
         assert self.sol.xorAfterQueries(nums, queries) == expected

    
    # def test_example_3(self):
    #     # TODO: Add test case
    #     pass
