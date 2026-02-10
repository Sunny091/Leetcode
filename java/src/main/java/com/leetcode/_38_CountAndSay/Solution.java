package com.leetcode._38_CountAndSay;

public class Solution {
    public static String countAndSay(int i) {
        if (i == 1) {
            return "1";
        }

        String prev = countAndSay(i - 1);
        StringBuilder result = new StringBuilder();

        char[] chars = prev.toCharArray();
        char current = chars[0];
        int count = 1;

        for (int j = 1; j < chars.length; j++) {
            if (chars[j] == current) {
                count++;
            } else {
                result.append(count).append(current);
                current = chars[j];
                count = 1;
            }
        }

        result.append(count).append(current);

        return result.toString();
    }
}
