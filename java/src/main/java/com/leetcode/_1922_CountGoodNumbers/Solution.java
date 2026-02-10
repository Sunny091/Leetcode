package com.leetcode._1922_CountGoodNumbers;

public class Solution {
    public static int countGoodNumbers(long n) {
        long mod = 1_000_000_007;
        long odd = n / 2;
        long even = (n % 2 == 0) ? odd : odd + 1;

        long oddPart = modPow(4, odd, mod);
        long evenPart = modPow(5, even, mod);

        return (int) ((oddPart * evenPart) % mod);
    }

    public static long modPow(long base, long exp, long mod) {
        long result = 1;
        base %= mod;

        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp >>= 1;
        }
        return result;
    }
}
