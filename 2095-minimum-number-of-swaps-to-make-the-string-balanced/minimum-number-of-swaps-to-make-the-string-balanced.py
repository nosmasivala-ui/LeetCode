class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for ch in s:
            if ch == "[":
                stack.append(ch)
            else:  # ch == "]"
                if stack:
                    stack.pop()

        return (len(stack) + 1) // 2
