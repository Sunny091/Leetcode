package com.leetcode._5_LongestPalindromicSubstring;

public class Solution {
    public static void main(String[] args) {
        String input = "babad";
        String result = longestPalindrome(input);
        System.out.println("Longest Palindromic Substring: " + result);
    }

    public static String longestPalindrome(String s) {
        int length = s.length();
        if (length == 0) return "";

        int start = 0, maxLength = 1;

        for (int i = 0; i < length; i++) {
            int l = i, r = i;
            while (l >= 0 && r < length && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > maxLength) {
                    start = l;
                    maxLength = r - l + 1;
                }
                l--;
                r++;
            }

            l = i;
            r = i + 1;
            while (l >= 0 && r < length && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > maxLength) {
                    start = l;
                    maxLength = r - l + 1;
                }
                l--;
                r++;
            }
        }

        return s.substring(start, start + maxLength);
    }
}
