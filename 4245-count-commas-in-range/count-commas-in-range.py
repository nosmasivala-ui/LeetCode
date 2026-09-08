class Solution:
    def countCommas(self, n: int) -> int:
        ranges = [
            (1000, 999_999, 1),
            (1_000_000, 999_999_999, 2),
            (1_000_000_000, 999_999_999_999, 3),
            (1_000_000_000_000, 999_999_999_999_999, 4),
        ]
        
        total = 0
        for start, end, commas in ranges:
            if n >= start:
                total += (min(n, end) - start + 1) * commas
        return total

