from typing import List


class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        """
        LeetCode 3474. Lexicographically Smallest Generated String

        TODO: Implement your solution here
        """
        n, m = len(str1), len(str2)
        L = n + m - 1

        ans = ['a'] * L
        fixed = [False] * L

        # 先處理 T
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if fixed[i + j] and ans[i + j] != str2[j]:
                        return ""
                    ans[i + j] = str2[j]
                    fixed[i + j] = True

        # 再處理 F
        for i in range(n):
            if str1[i] == 'F':
                if ''.join(ans[i:i + m]) == str2:
                    changed = False
                    # 從右往左改，滿足 lexicographically smallest
                    for j in range(m - 1, -1, -1):
                        pos = i + j
                        if not fixed[pos]:
                            ans[pos] = 'b' if str2[j] == 'a' else 'a'
                            changed = True
                            break
                    if not changed:
                        return ""

        # 最後再驗證一次
        res = ''.join(ans)
        for i in range(n):
            if (res[i:i + m] == str2) != (str1[i] == 'T'):
                return ""

        return res