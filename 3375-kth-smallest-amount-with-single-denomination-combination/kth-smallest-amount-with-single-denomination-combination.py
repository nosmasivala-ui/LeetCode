class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count(x: int) -> int:
            total = 0
            n = len(coins)

            for r in range(1, n + 1):
                for comb in combinations(coins, r):
                    lcm = comb[0]
                    for c in comb[1:]:
                        lcm = lcm * c // gcd(lcm, c)
                    total += (x // lcm) * (-1 if r % 2 == 0 else 1)
            return total

        left, right = 1, 10**18  
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left
