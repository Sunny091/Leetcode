package com.leetcode._6_ZigzagConversion;

public class Solution {
    // 測試主程式
    public static void main(String[] args) {
        String input = "PAYPALISHIRING";
        int numRows = 3;
        String converted = convert(input, numRows);
        System.out.println("Converted: " + converted);
    }

    public static String convert(String s, int numRows) {
        if (numRows == 1)
            return s;

        int sLength = s.length();
        StringBuilder result = new StringBuilder();
        int cycleLen = 2 * numRows - 2;

        for (int i = 0; i < numRows; i++) {
            for (int j = i; j < sLength; j += cycleLen) {
                result.append(s.charAt(j));

                // 處理中間行需額外插入的字元
                int secondIndex = j + cycleLen - 2 * i;
                if (i != 0 && i != numRows - 1 && secondIndex < sLength) {
                    result.append(s.charAt(secondIndex));
                }
            }
        }

        return result.toString();
    }

}
