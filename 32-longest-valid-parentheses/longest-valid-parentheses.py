class Solution:
    def longestValidParentheses(self, s: str) -> int:
        count_1 = 0   
        count_2 = 0   
        max_len = 0   

        for i in range(len(s)):
            if s[i] == '(':
                count_1 += 1
            else:
                count_2 += 1
            if count_1 == count_2:
                max_len = max(max_len, count_1 + count_2)
            elif count_2 > count_1:
                count_1 = 0
                count_2 = 0

        count_1 = 0
        count_2 = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == '(':
                count_1 += 1
            else:
                count_2 += 1
            if count_1 == count_2:
                max_len = max(max_len, count_1 + count_2)
            elif count_1 > count_2:
                count_1 = 0
                count_2 = 0

        return max_len




