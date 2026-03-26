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
        word1 = "abc"
        word2 = "bca"
        assert self.sol.closeStrings(word1, word2) == True

    def test_example_2(self):
        # TODO: Add test case
        word1 = "a"
        word2 = "aa"
        assert self.sol.closeStrings(word1, word2) == False

    def test_example_3(self):
        # TODO: Add test case
        word1 = "cabbba"
        word2 = "abbccc"
        assert self.sol.closeStrings(word1, word2) == True
