package com.leetcode._38_CountAndSay;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    public void Test1() {
        assertEquals("1211", Solution.countAndSay(4));
    }

    @Test
    public void Test2() {
        assertEquals("1", Solution.countAndSay(1));
    }
}
