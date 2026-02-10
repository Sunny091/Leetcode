package com.leetcode._1534_CountGoodTriplets;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    public void Test1() {
        int[] array = { 3, 0, 1, 1, 9, 7 };
        assertEquals(4, Solution.countGoodTriplets(array, 7, 2, 3));
    }

    @Test
    public void Test2() {
        int[] array = { 1, 1, 2, 2, 3 };
        assertEquals(0, Solution.countGoodTriplets(array, 0, 0, 1));
    }

    @Test
    public void Test3() {
        int[] array = { 7, 3, 7, 3, 12, 1, 12, 2, 3 };
        assertEquals(12, Solution.countGoodTriplets(array, 5, 8, 1));
    }
}
