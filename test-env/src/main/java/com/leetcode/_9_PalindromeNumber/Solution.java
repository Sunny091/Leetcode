package com.leetcode._9_PalindromeNumber;

public class Solution {
    public static boolean isPalindrome(int x) {
        // �t�Ƥ��O�^���
        if (x < 0)
            return false;

        // ���ƥû��O�^���
        if (x < 10)
            return true;

        int temp = x;
        int result = 0;

        while (temp != 0) {
            int digit = temp % 10;
            // �ˬd�O�_�|����]�i��AJava int �w�]�O 32-bit�A����ᤣ�|�j��d��^
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
