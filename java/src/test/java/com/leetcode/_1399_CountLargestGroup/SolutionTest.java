package com.leetcode._1399_CountLargestGroup;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    public void Test1() {
        assertEquals(4, Solution.countLargestGroup(13));
    }

    @Test
    public void Test2() {
        assertEquals(2, Solution.countLargestGroup(2));
    }
}
