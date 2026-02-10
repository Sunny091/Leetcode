package com.leetcode._781_RabbitsInForest;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    public void Test1() {
        int[] nums = { 1, 1, 2 };
        assertEquals(5, Solution.numRabbits(nums));
    }

    @Test
    public void Test2() {
        int[] nums = { 10, 10, 10 };
        assertEquals(11, Solution.numRabbits(nums));
    }
}
