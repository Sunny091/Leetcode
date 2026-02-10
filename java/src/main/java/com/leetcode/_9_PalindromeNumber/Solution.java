package com.leetcode._9_PalindromeNumber;

public class Solution {
    public static boolean isPalindrome(int x) {
        // 負數不是回文數
        if (x < 0)
            return false;

        // 單位數永遠是回文數
        if (x < 10)
            return true;

        int temp = x;
        int result = 0;

        while (temp != 0) {
            int digit = temp % 10;
            // 檢查是否會溢位（可選，Java int 預設是 32-bit，反轉後不會大於範圍）
            result = result * 10 + digit;
            temp /= 10;
        }

        return result == x;
    }

    public static void main(String[] args) {
        int number = 121;
        System.out.println("Is " + number + " a palindrome? " + isPalindrome(number)); // true

        number = -121;
        System.out.println("Is " + number + " a palindrome? " + isPalindrome(number)); // false

        number = 123;
        System.out.println("Is " + number + " a palindrome? " + isPalindrome(number)); // false
    }
}
