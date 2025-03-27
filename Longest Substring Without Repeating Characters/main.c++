#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int lengthOfLongestSubstring(const std::string& s) {
    int length = s.length();
    if (length == 0)
        return 0;
    if (length == 1)
        return 1;

    std::vector<int> array(length, -1);

    for (int i = 0; i < length; ++i) {
        int j = i - 1;
        while (j >= 0 && s[i] != s[j]) {
            --j;
        }
        array[i] = j;
    }

    int result = 0;
    int start = 0, now = 1;

    while (now < length) {
        while (now < length && array[now] < start) {
            ++now;
        }
        int temp = now - start;
        result = std::max(result, temp);
        ++start;
    }

    return result;
}

int main() {
    std::string input;
    std::cout << "Enter string: ";
    std::cin >> input;

    int result = lengthOfLongestSubstring(input);
    std::cout << "Length of longest substring without repeating characters: "
              << result << std::endl;

    return 0;
}
