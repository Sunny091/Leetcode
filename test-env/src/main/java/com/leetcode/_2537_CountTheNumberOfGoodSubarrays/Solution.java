package com.leetcode._2537_CountTheNumberOfGoodSubarrays;

import java.util.HashMap;
import java.util.Map;

public class Solution {

    public static long countGood(int[] nums, int k) {
        int left = 0;
        long pairs = 0;
        long result = 0;
        Map<Integer, Integer> freq = new HashMap<>();
        for (int right = 0; right < nums.length; right++) {
            int number = nums[right];
            int count = freq.getOrDefault(number, 0);
            pairs += count;
            freq.put(number, count + 1);
            while (pairs >= k) {
                result += nums.length - right;
                int lnumber = nums[left];
                int lcount = freq.get(lnumber);
                freq.put(lnumber, lcount - 1);
                pairs -= (lcount - 1);
                left++;
            }
        }
        return result;
    }
}
