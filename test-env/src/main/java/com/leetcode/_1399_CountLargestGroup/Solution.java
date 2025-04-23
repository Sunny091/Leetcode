package com.leetcode._1399_CountLargestGroup;

public class Solution {
    public static Integer countLargestGroup(int n) {
        int answer = 0;
        int[] map = new int[37];
        for (int i = 1; i <= n; i++) {
            int digit = digitAddition(i);
            map[digit]++;
        }
        int max = 0;
        for (int value : map) {
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
