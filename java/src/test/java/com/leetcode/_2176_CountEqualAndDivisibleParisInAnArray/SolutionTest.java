package com.leetcode._2176_CountEqualAndDivisibleParisInAnArray;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    public void Test1() {
        int[] nums = { 3, 1, 2, 2, 2, 1, 3 };
        assertEquals(4, Solution.countPairs(nums, 2));
    }

    @Test
    public void Test2() {
        int[] nums = { 1, 2, 3, 4 };
        assertEquals(0, Solution.countPairs(nums, 1));
    }
}
