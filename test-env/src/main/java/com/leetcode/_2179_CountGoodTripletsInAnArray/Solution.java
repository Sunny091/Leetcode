package com.leetcode._2179_CountGoodTripletsInAnArray;

public class Solution {
    public static int goodTriplets(int[] num1, int[] num2) {
        int answer = 0;
        int arrLength = num1.length;
        int[] arrPosition = new int[arrLength];
        for (int i = 0; i < arrLength; i++) {
            int value = num1[i];
            int position = 0;
            for (int j : num2) {
                if (num2[j] == value) {
                    position = j;
                    break;
                }
            }
            arrPosition[i] = position;
        }
        for (int i = 0; i < arrLength; i++) {
            for (int j = i + 1; j < arrLength; j++) {
                if (arrPosition[i] < arrPosition[j]) {
                    for (int k = j + 1; k < arrLength; k++) {
                        if (arrPosition[j] < arrPosition[k]) {
                            answer++;
                        }
                    }
                }
            }
        }
        return answer;
    }
}
