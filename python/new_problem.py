#!/usr/bin/env python3
"""
Script to create a new LeetCode problem template.

Usage:
    python new_problem.py 123 TwoSum
    python new_problem.py 2799 CountCompleteSubarrayInAnArray
"""

import os
import sys
from pathlib import Path

SOLUTION_TEMPLATE = '''from typing import List


class Solution:
    def {method_name}(self):
        """
        LeetCode {number}. {title}

        TODO: Implement your solution here
        """
        pass
'''

TEST_TEMPLATE = '''import pytest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from solution import Solution


class TestSolution:
    def setup_method(self):
        self.sol = Solution()

    def test_example_1(self):
        # TODO: Add test case
        pass

    def test_example_2(self):
        # TODO: Add test case
        pass
'''


def to_camel_case(name: str) -> str:
    """Convert PascalCase to camelCase for method name."""
    if not name:
        return name
    return name[0].lower() + name[1:]


def create_problem(number: str, title: str):
    problems_dir = Path(__file__).parent / "problems"
    problem_dir = problems_dir / f"_{number}_{title}"

    if problem_dir.exists():
        print(f"Problem directory already exists: {problem_dir}")
        return

    problem_dir.mkdir(parents=True, exist_ok=True)

    # Create __init__.py
    (problem_dir / "__init__.py").touch()

    # Create solution.py
    method_name = to_camel_case(title)
    solution_content = SOLUTION_TEMPLATE.format(
        method_name=method_name,
        number=number,
        title=title.replace("_", " ")
    )
    (problem_dir / "solution.py").write_text(solution_content)

    # Create test_solution.py
    (problem_dir / "test_solution.py").write_text(TEST_TEMPLATE)

    print(f"Created problem: {problem_dir}")
    print(f"  - solution.py")
    print(f"  - test_solution.py")


def main():
    if len(sys.argv) != 3:
        print("Usage: python new_problem.py <number> <ProblemTitle>")
        print("Example: python new_problem.py 1 TwoSum")
        sys.exit(1)

    number = sys.argv[1]
    title = sys.argv[2]
    create_problem(number, title)


if __name__ == "__main__":
    main()
