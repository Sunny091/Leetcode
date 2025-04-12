package com.leetcode._3272_FindtheCountofGoodIntegers;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class SolutionTest {
    @Test
    public void Test1() {
        assertEquals(27, Solution.countGoodIntegers(3, 5));
    }

    @Test
    public void Test2() {
        assertEquals(2, Solution.countGoodIntegers(1, 4));
    }

    @Test
    public void Test3() {
        assertEquals(2468, Solution.countGoodIntegers(5, 6));
    }
}
