class Solution:
    def isValid(self, s: str) -> bool:
        # while "()" in s or "[]" in s or "{}" in s:
        #     s = s.replace("()", "").replace("[]", "").replace("{}", "")
        # return s == ""
        
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if pairs[ch] != top:
                    return False

        return not stack



