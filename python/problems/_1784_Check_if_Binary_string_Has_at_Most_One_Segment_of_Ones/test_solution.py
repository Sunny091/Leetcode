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
        s = "1001"
        expected = False
        assert self.sol.checkOnesSegment(s) == expected

    def test_example_2(self):
        # TODO: Add test case
        s = "110"
        expected = True
        assert self.sol.checkOnesSegment(s) == expected

    # def test_example_3(self):
    #     # TODO: Add test case
    #     pass
