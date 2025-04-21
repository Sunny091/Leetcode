package com.leetcode._2563_CountTheNumberOfFairPairs;

import java.util.Arrays;

public class Solution {
    public static long countFairPairs(int[] nums, int lower, int upper) {
        Arrays.sort(nums);
        long result = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            int start = i + 1;
            while (start < nums.length && nums[i] + nums[start] < lower) {
                start++;
            }

            int end = nums.length - 1;
            while (end >= start && nums[i] + nums[end] > upper) {
                end--;
            }

            if (start <= end) {
                result += (end - start + 1);
            }
        }
        return result;
    }
}
