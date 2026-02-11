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
        s = "the sky is blue"
        assert self.sol.reverseWords(s) == "blue is sky the"

    def test_example_2(self):
        # TODO: Add test case
        s = "  hello world  "
        assert self.sol.reverseWords(s) == "world hello"
    
    def test_example_3(self):
        # TODO: Add test case
        s = "a good   example"
        assert self.sol.reverseWords(s) == "example good a"
