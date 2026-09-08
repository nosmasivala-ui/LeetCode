class Solution:
    def repeatedCharacter(self, s: str) -> str:
        n = set()
        
        for ch in s:
            if ch in n:
                return ch
            n.add(ch)