package com.leetcode._2843_CountSymmetricIntegers;

public class Solution {
    public static int countSymmetricIntegers(int low, int high) {
        int answer = 0;
        for (int i = low; i <= high; i++) {
            int digit = countDigit(i);
            if (digit % 2 == 0) {
                int leftSum = 0, rightSum = 0;
                int num = i; // ?? num ?�]?s i
                for (int j = 0; j < digit / 2; j++) {
                    rightSum += num % 10;
                    num /= 10;
                }
                for (int j = 0; j < digit / 2; j++) {
                    leftSum += num % 10;
                    num /= 10;
                }
                if (rightSum == leftSum) {
                    answer += 1;
                }
            }
        }
        return answer;
    }

    public static int countDigit(int num) {
        int digit = 0;
        while (num != 0) {
            digit++;
            num /= 10;
        }
        return digit;
    }
}
