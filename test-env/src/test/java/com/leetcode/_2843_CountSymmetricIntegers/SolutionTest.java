package com.leetcode._2843_CountSymmetricIntegers;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class SolutionTest {

    @Test
    public void testRange1To100() {
        assertEquals(9, Solution.countSymmetricIntegers(1, 100));
    }

    @Test
    public void testRange1200To1234() {
        assertEquals(4, Solution.countSymmetricIntegers(1200, 1234));
    }

    @Test
    public void testRangeWithNoSymmetric() {
        assertEquals(0, Solution.countSymmetricIntegers(101, 999));
    }

    @Test
    public void testSingleSymmetricNumber() {
        assertEquals(1, Solution.countSymmetricIntegers(11, 11)); // 11 is symmetric
    }
}
