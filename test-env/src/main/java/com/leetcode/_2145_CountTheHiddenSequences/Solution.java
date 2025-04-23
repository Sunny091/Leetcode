package com.leetcode._2145_CountTheHiddenSequences;

public class Solution {
    public static Integer numberOfArrays(int[] diffences, int lower, int upper) {
        int count = 0;
        int range = upper - lower;
        int fixLower = 0;
        int fixUpper = 0;
        for (int num : diffences) {
            count += num;
            if (count < fixLower) {
                if (count < -range) {
                    return 0;
                }
                fixLower = count;
            } else if (count > fixUpper) {
                if (count>range) {
                    return 0;
                }
                fixUpper = count;
            }
        }
        return Math.max(0, (upper - fixUpper) - (lower - fixLower) + 1);
    }
}
