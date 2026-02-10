package com.leetcode._7_ReverseInteger;

public class Solution {
    public static int reverse(int x) {
        int result = 0;

        while (x != 0) {
            int digit = x % 10;
            x /= 10;

            // 檢查是否會溢位
            if (result > Integer.MAX_VALUE / 10 || (result == Integer.MAX_VALUE / 10 && digit > 7)) {
                return 0;
            }
            if (result < Integer.MIN_VALUE / 10 || (result == Integer.MIN_VALUE / 10 && digit < -8)) {
                return 0;
            }

            result = result * 10 + digit;
        }

        return result;
    }

    // 測試用 main
    public static void main(String[] args) {
        int input = 123;
        int output = reverse(input);
        System.out.println("Reversed: " + output);
    }
}
