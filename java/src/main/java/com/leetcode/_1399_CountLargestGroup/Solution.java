package com.leetcode._1399_CountLargestGroup;

public class Solution {
    public static Integer countLargestGroup(int n) {
        int answer = 0;
        int[] map = new int[37];
        for (int i = 1; i <= n; i++) {
            int sum = 0, x = i;
            while (x > 0) {
                sum += x % 10;
                x /= 10;
            }
            map[sum]++;
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
}
