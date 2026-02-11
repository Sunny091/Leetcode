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
        word2 = "pqr"
        assert self.sol.mergeAlternately(word1, word2) == "apbqcr"

    def test_example_2(self):
        # TODO: Add test case
        word1 = "ab"
        word2 = "pqrs"
        assert self.sol.mergeAlternately(word1, word2) == "apbqrs"

    def test_example_3(self):
        # TODO: Add test case
        word1 = "abcd"
        word2 = "pq"
        assert self.sol.mergeAlternately(word1, word2) == "apbqcd"
