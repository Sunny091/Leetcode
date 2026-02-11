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
        str1 = "ABCABC"
        str2 = "ABC"
        assert self.sol.gcdOfStrings(str1, str2) == "ABC"

    def test_example_2(self):
        # TODO: Add test case
        str1 = "ABABAB"
        str2 = "ABAB"
        assert self.sol.gcdOfStrings(str1, str2) == "AB"

    def test_example_3(self):
        # TODO: Add test case
        str1 = "LEET"
        str2 = "CODE"
        assert self.sol.gcdOfStrings(str1, str2) == ""

    def test_example_4(self):
        # TODO: Add test case
        str1 = "AAAAAB"
        str2 = "AAA"
        assert self.sol.gcdOfStrings(str1, str2) == ""
