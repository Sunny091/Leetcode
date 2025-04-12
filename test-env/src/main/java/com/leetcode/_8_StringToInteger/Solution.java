package com.leetcode._8_StringToInteger;

public class Solution {
    public static int myAtoi(String s) {
        int i = 0, result = 0, sign = 1;
        int n = s.length();

        // ���L�e�ɪŮ�
        while (i < n && s.charAt(i) == ' ') {
            i++;
        }

        // �B�z���t��
        if (i < n && (s.charAt(i) == '-' || s.charAt(i) == '+')) {
            sign = (s.charAt(i) == '-') ? -1 : 1;
            i++;
        }

        // �B�z�Ʀr����
        while (i < n && Character.isDigit(s.charAt(i))) {
            int digit = s.charAt(i) - '0';

            // �ˬd����
            if (result > (Integer.MAX_VALUE - digit) / 10) {
                return (sign == 1) ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }

            result = result * 10 + digit;
            i++;
        }

        return result * sign;
    }

    public static void main(String[] args) {
        String input = "   -42";
        int output = myAtoi(input);
        System.out.println("Converted: " + output); // Output: -42
    }
}
