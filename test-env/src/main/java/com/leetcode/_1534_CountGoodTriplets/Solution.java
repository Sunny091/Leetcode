package com.leetcode._1534_CountGoodTriplets;

public class Solution {
    public static int countGoodTriplets(int[] arr, int a, int b, int c) {
        int answer = 0;
        for (int i = 0; i < arr.length - 2; i++) {
            for (int k = i + 2; k < arr.length; k++) {
                if (Math.abs(arr[i] - arr[k]) <= c) {
                    for (int j = i + 1; j < k; j++) {
                        if (Math.abs(arr[i] - arr[j]) <= a && Math.abs(arr[j] - arr[k]) <= b) {
                            answer++;
                        }
                    }
                }
            }
        }
        return answer;
    }
}
