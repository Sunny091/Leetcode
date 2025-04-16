package com.leetcode._2537_CountTheNumberOfGoodSubarrays;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    public void Test1() {
        int[] arr = { 1, 1, 1, 1, 1 };
        assertEquals(1, Solution.countGood(arr, 10));
    }

    @Test
    public void Test2() {
        int[] arr = { 3, 1, 4, 3, 2, 2, 4 };
        assertEquals(4, Solution.countGood(arr, 2));
    }
}
