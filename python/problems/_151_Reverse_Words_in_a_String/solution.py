from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        """
        LeetCode 151. Reverse Words in a String

        TODO: Implement your solution here
        """
        length = len(s)
        start_index = length - 1
        end_index = length - 1
        answer = ""
        for i in reversed(range(length)):
            if s[i] == " ":
                start_index = i + 1
                if end_index >= start_index:
                    answer += s[start_index: end_index + 1] + " "
                end_index = i - 1
        if end_index >= 0:
            answer += s[0: end_index + 1]
        return answer.strip()
