package com.leetcode._3_LongestSubstringWithoutRepeatingCharacters;

import java.util.Scanner;

public class Solution {
    public static int lengthOfLongestSubstring(String s) {
        int length = s.length();
        if (length == 0)
            return 0;
        if (length == 1)
            return 1;

        int[] array = new int[length];
        for (int i = 0; i < length; i++) {
            int j = i - 1;
            while (j >= 0 && s.charAt(i) != s.charAt(j)) {
                j--;
            }
            array[i] = j;
        }

        int result = 0;
        int start = 0, now = 1;

        while (now < length) {
            while (now < length && array[now] < start) {
                now++;
            }
            int temp = now - start;
            result = Math.max(result, temp);
            start++;
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter string: ");
        String input = scanner.nextLine();

        int result = lengthOfLongestSubstring(input);
        System.out.println(
                "Length of longest substring without repeating characters: " +
                        result);

        scanner.close();
    }
}
