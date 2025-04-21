package com.leetcode._2563_CountTheNumberOfFairPairs;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    public void Test1() {
        int[] nums = { 0, 1, 7, 4, 4, 5 };
        assertEquals(6, Solution.countFairPairs(nums, 3, 6));
    }

    @Test
    public void Test2() {
        int[] nums = { 1, 7, 9, 2, 5 };
        assertEquals(1, Solution.countFairPairs(nums, 11, 11));
    }
}
