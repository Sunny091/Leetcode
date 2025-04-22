package com.leetcode._2563_CountTheNumberOfFairPairs;

import java.util.Arrays;

public class Solution {
    public static long countFairPairs(int[] nums, int lower, int upper) {
        Arrays.sort(nums);
        long result = 0;
        for (int i = 0; i < nums.length; i++) {
            long left = leftIndex(nums, i + 1, nums.length - 1, lower - nums[i]);
            long right = rightIndex(nums, i + 1, nums.length - 1, upper - nums[i]);
            if (left <= right) {
                result += (right - left + 1);
            }
        }
        return result;
    }

    public static long leftIndex(int[] nums, int low, int high, int target) {
        while (low <= high) {
            int mid = (low + high) >>> 1;
            if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return low;
    }

    private static long rightIndex(int[] nums, int low, int high, int target) {
        while (low <= high) {
            int mid = (low + high) >>> 1;
            if (nums[mid] <= target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return high;
    }
}
