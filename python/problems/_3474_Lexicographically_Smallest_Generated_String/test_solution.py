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
        str1 = "TFTF"
        str2 = "ab"
        assert self.sol.generateString(str1, str2) == "ababa"

    def test_example_2(self):
        # TODO: Add test case
        str1 = "TFTF"
        str2 = "abc"
        assert self.sol.generateString(str1, str2) == ""
    
    def test_example_3(self):
        # TODO: Add test case
        str1 = "F"
        str2 = "d"
        assert self.sol.generateString(str1, str2) == "a"

    def test_example_4(self):
        str1 = "FTF"
        str2 = "xww"
        assert self.sol.generateString(str1, str2) == "axwwa"