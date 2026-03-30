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
        s1 = "abcdba"
        s2 = "cabdab"
        assert self.sol.checkStrings(s1, s2) == True

    def test_example_2(self):
        # TODO: Add test case
        s1 = "abe"
        s2 = "bea"
        assert self.sol.checkStrings(s1, s2) == False

    # def test_example_3(self):
    #     # TODO: Add test case
    #     pass
