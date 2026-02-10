package com.leetcode._2799_CountCompleteSubarrayInAnArray;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    public void Test1() {
        int[] nums = { 1, 3, 1, 2, 2 };
        assertEquals(4, Solution.countCompleteSubarrays(nums));
    }

    @Test
    public void Test2() {
        int[] nums = { 5, 5, 5, 5 };
        assertEquals(10, Solution.countCompleteSubarrays(nums));
    }
}
