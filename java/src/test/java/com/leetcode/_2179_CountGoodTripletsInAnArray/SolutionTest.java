package com.leetcode._2179_CountGoodTripletsInAnArray;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    public void Test1() {
        int[] num1 = { 2, 0, 1, 3 };
        int[] num2 = { 0, 1, 2, 3 };
        assertEquals(1, Solution.goodTriplets(num1, num2));
    }

    @Test
    public void Test2() {
        int[] num1 = { 4, 0, 1, 3, 2 };
        int[] num2 = { 4, 1, 0, 2, 3 };
        assertEquals(4, Solution.goodTriplets(num1, num2));
    }

    @Test
    public void Test3() {
        int[] num1 = { 13, 14, 10, 2, 12, 3, 9, 11, 15, 8, 4, 7, 0, 6, 5, 1 };
        int[] num2 = { 8, 7, 9, 5, 6, 14, 15, 10, 2, 11, 4, 13, 3, 12, 1, 0 };
        assertEquals(77, Solution.goodTriplets(num1, num2));
    }
}
