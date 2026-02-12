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
        flowerbed = [1,0,0,0,1]
        n = 1
        assert self.sol.canPlaceFlowers(flowerbed, n) == True

    def test_example_2(self):
        # TODO: Add test case
        flowerbed = [1,0,0,0,1]
        n = 2
        assert self.sol.canPlaceFlowers(flowerbed, n) == False
    
    def test_example_3(self):
        # TODO: Add test case
        flowerbed = [1,0]
        n = 1
        assert self.sol.canPlaceFlowers(flowerbed, n) == False
