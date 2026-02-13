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
        s = "IceCreAm"
        assert self.sol.reverseVowels(s) == "AceCreIm"

    def test_example_2(self):
        # TODO: Add test case
        s = "leetcode"
        assert self.sol.reverseVowels(s) == "leotcede"
    
    # def test_example_3(self):
    #     # TODO: Add test case
    #     pass
