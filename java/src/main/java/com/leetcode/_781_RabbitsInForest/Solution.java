package com.leetcode._781_RabbitsInForest;

import java.util.HashMap;
import java.util.Map;

public class Solution {

    public static int numRabbits(int[] answers) {
        Map<Integer, Integer> map = new HashMap<>();
        int result = 0;

        for (int num : answers) {
            if (num == 0) {
                result++;
            } else if (!map.containsKey(num)) {
                map.put(num, 1);
                result += num + 1;
            } else {
                map.put(num, map.get(num) + 1);
                if (map.get(num) == num + 1) {
                    map.remove(num);
                }
            }
        }

        return result;
    }
}
