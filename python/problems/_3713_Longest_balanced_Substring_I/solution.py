from typing import List


class Solution:
    def longestBalanced(self, s: str) -> int:
        """
        LeetCode 3713. Longest balanced Substring I

        TODO: Implement your solution here
        """
        answer = 0
        length = len(s)
        candidate = set()
        for i in range(length):
            candidate.clear()
            max_frequency = 1
            count = [0] * 26
            temp_answer = 0
            for j in range(i, length):
                index = ord(s[j]) - 97
                count[index] += 1
                if count[index] == max_frequency:
                    if s[j] in candidate:
                        candidate.remove(s[j])
                    if not candidate:
                        temp_answer = j - i + 1
                elif count[index] < max_frequency:
                    candidate.add(s[j])
                else:
                    max_frequency = count[index]
                    candidate = {chr(
                        x + 97) for x in range(26) if count[x] < max_frequency and count[x] > 0 and x != index}
                    if not candidate:
                        temp_answer = j - i + 1
            answer = max(answer, temp_answer)
        return answer
