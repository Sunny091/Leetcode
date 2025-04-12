package com.leetcode._11_ContainerWithMostWater;

public class Solution {
    public static int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int maxResult = 0;
        int temp, now;

        while (right > left) {
            temp = (right - left) * Math.min(height[left], height[right]);
            maxResult = Math.max(maxResult, temp);

            if (height[right] > height[left]) {
                now = height[left];
                while (left < right && height[++left] <= now) {
                }
            } else if (height[right] < height[left]) {
                now = height[right];
                while (left < right && height[--right] <= now) {
                }
            } else {
                right--;
                left++;
            }
        }

        return maxResult;
    }

    public static void main(String[] args) {
        int[] height = { 1, 8, 6, 2, 5, 4, 8, 3, 7 };
        System.out.println(maxArea(height)); // Output: 49
    }
}
