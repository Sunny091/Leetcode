
class Solution:
    def longestBalanced(self, s: str) -> int:
        """
        LeetCode 3714. Long Balanced Substring II

        TODO: Implement your solution here
        """
        length = len(s)
        answer = 0

        for i in range(length):
            if answer >= (length - i):
                return answer
            record = [0] * 26
            max_freq = 0
            num_distinct = 0
            for j in range(i, length):
                c_index = ord(s[j]) - ord('a')
                if record[c_index] == 0:
                    num_distinct += 1
                record[c_index] += 1
                if record[c_index] > max_freq:
                    max_freq = record[c_index]
                # 若 max_freq * 不同字母數 == 子字串長度，代表所有字母出現次數相同
                if max_freq * num_distinct == (j - i + 1):
                    answer = max(answer, j - i + 1)

        return answer
