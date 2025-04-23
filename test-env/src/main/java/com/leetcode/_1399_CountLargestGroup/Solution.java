package com.leetcode._1399_CountLargestGroup;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public static Integer countLargestGroup(int n) {
        int answer = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            int digit = digitAddition(i);
            if (!map.containsKey(digit)) {
                map.put(digit, 1);
            } else {
                map.put(digit, map.get(digit) + 1);
            }
        }
        int max = 0;
        for (int value : map.values()) {
            if (value > max) {
                max = value;
                answer = 1;
            } else if (value == max) {
                answer++;
            }
        }
        return answer;
    }

    public static int digitAddition(int n) {
        int result = 0;
        while (n > 0) {
            int temp = n % 10;
            result += temp;
            n /= 10;
        }
        return result;
    }
}
