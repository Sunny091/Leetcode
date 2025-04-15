package com.leetcode._3272_FindtheCountofGoodIntegers;

import java.util.*;

public class Solution {
    static Set<String> numSet = new HashSet<>(); // �Ψӥh�� digit �զX
    static int[] numArray = new int[10]; // �����U��ƥX�{����
    static long[] facArray = new long[11]; // ���h�֨��]�̦h�� 10!�^

    public static long countGoodIntegers(int n, int k) {
        int low = (int) Math.pow(10, n - 1);
        int high = (int) Math.pow(10, n);
        numSet.clear(); // �C���I�s�M�Ťw�ιL�զX
        long answer = 0;

        for (int i = low; i < high; i++) {
            if (i % k == 0 && isPalindromic(i)) {
                String key = encodeCount(numArray);
                if (numSet.add(key)) {
                    // ���ըC�ӫD 0 �Ʀr����
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
                        numArray[firstDigit]++; // �٭�
                    }
                    answer += validTotal;
                }
            }
        }

        return answer;
    }

    // �P�_�O�_���^��A�òέp�U�Ʀr�X�{����
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

    // �N numArray �s�X���ߤ@�r��@�� Set key
    public static String encodeCount(int[] count) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 10; i++) {
            sb.append(count[i]).append('#');
        }
        return sb.toString();
    }

    // �p�ⶥ�h�ç֨�
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