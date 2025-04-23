package com.leetcode._2145_CountTheHiddenSequences;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    public void Test1() {
        int[] diffence = { 1, -3, 4 };
        assertEquals(2, Solution.numberOfArrays(diffence, 1, 6));
    }

    @Test
    public void Test2() {
        int[] diffence = { 3, -4, 5, 1, -2 };
        assertEquals(4, Solution.numberOfArrays(diffence, -4, 5));
    }
    
    @Test
    public void Test3() {
        int[] diffence = { 4,-7,2};
        assertEquals(0, Solution.numberOfArrays(diffence, 3, 6));
    }
}
