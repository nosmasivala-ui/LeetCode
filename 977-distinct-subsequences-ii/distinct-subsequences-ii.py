class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        total = 0
        last = {}

        for ch in s:
            new_total = (total + 1) % MOD  
            if ch in last:
                new_total = (total + 1 - last[ch]) % MOD
            last[ch] = (total + 1) % MOD
            total = (total + new_total) % MOD

        return total % MOD
