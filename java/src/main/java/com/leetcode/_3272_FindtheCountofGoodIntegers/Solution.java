package com.leetcode._3272_FindtheCountofGoodIntegers;

import java.util.*;

public class Solution {
    static Set<String> numSet = new HashSet<>(); // 用來去重 digit 組合
    static int[] numArray = new int[10]; // 紀錄各位數出現次數
    static long[] facArray = new long[11]; // 階層快取（最多到 10!）

    public static long countGoodIntegers(int n, int k) {
        int low = (int) Math.pow(10, n - 1);
        int high = (int) Math.pow(10, n);
        numSet.clear(); // 每次呼叫清空已用過組合
        long answer = 0;

        for (int i = low; i < high; i++) {
            if (i % k == 0 && isPalindromic(i)) {
                String key = encodeCount(numArray);
                if (numSet.add(key)) {
                    // 嘗試每個非 0 數字當首位
                    long validTotal = 0;
                    for (int firstDigit = 1; firstDigit <= 9; firstDigit++) {
                        if (numArray[firstDigit] == 0)
                            continue;

                        numArray[firstDigit]--;
                        long count = factorial(n - 1);
                        for (int j = 0; j < 10; j++) {
                            if (numArray[j] > 1) {
                                count /= factorial(numArray[j]);
                            }
                        }
                        validTotal += count;
                        numArray[firstDigit]++; // 還原
                    }
                    answer += validTotal;
                }
            }
        }

        return answer;
    }

    // 判斷是否為回文，並統計各數字出現次數
    public static boolean isPalindromic(int number) {
        Arrays.fill(numArray, 0);
        int original = number;
        int reversed = 0;

        while (number != 0) {
            int digit = number % 10;
            numArray[digit]++;
            reversed = reversed * 10 + digit;
            number /= 10;
        }

        return reversed == original;
    }

    // 將 numArray 編碼成唯一字串作為 Set key
    public static String encodeCount(int[] count) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 10; i++) {
            sb.append(count[i]).append('#');
        }
        return sb.toString();
    }

    // 計算階層並快取
    public static long factorial(int n) {
        if (facArray[n] != 0)
            return facArray[n];
        long res = 1;
        for (int i = 2; i <= n; i++)
            res *= i;
        facArray[n] = res;
        return res;
    }
}