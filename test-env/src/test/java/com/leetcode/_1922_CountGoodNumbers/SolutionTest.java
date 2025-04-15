package com.leetcode._1922_CountGoodNumbers;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class SolutionTest {
    @Test
    public void Test1() {
        assertEquals(5, Solution.countGoodNumbers(1));
    }

    @Test
    public void Test2() {
        assertEquals(400, Solution.countGoodNumbers(4));
    }

    @Test
    public void Test3() {
        assertEquals(564908303, Solution.countGoodNumbers(50));
    }
}
