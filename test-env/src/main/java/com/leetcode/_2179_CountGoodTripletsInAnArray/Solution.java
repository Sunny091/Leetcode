package com.leetcode._2179_CountGoodTripletsInAnArray;

class Solution {
    static class BIT {
        int[] tree;

        public BIT(int size) {
            tree = new int[size + 2];
        }

        public void update(int index, int delta) {
            for (index += 1; index < tree.length; index += index & -index) {
                tree[index] += delta;
            }
        }

        public int query(int index) {
            int sum = 0;
            for (index += 1; index > 0; index -= index & -index) {
                sum += tree[index];
            }
            return sum;
        }

        public int queryRange(int left, int right) {
            return query(right) - query(left - 1);
        }
    }

    public static long goodTriplets(int[] num1, int[] num2) {
        int n = num1.length;
        int[] pos = new int[n];
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            pos[num1[i]] = i;
        }
        for (int i = 0; i < n; i++) {
            arr[i] = pos[num2[i]];
        }

        long answer = 0;
        long[] leftSmaller = new long[n];
        BIT bit = new BIT(n);

        for (int i = 0; i < n; i++) {
            leftSmaller[i] = bit.query(arr[i] - 1);
            bit.update(arr[i], 1);
        }

        bit = new BIT(n); // reset
        for (int i = n - 1; i >= 0; i--) {
            long rightLarger = bit.queryRange(arr[i] + 1, n);
            answer += leftSmaller[i] * rightLarger;
            bit.update(arr[i], 1);
        }

        return answer;
    }
}
