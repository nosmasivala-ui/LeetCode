class Solution:
    def checkValidString(self, s: str) -> bool:
        stack1 = []  
        stack2 = [] 

        for i in range(len(s)):
            ch = s[i]
            if ch == "(":
                stack1.append(i)
            elif ch == "*":
                stack2.append(i)
            else:  # ch == ")"
                if stack1:
                    stack1.pop()
                elif stack2:
                    stack2.pop()
                else:
                    return False

        while stack1 and stack2:
            if stack1[-1] < stack2[-1]:
                stack1.pop()
                stack2.pop()
            else:
                return False

        return not stack1


            