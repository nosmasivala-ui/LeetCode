class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_map = defaultdict(set)
        for row, seat in reservedSeats:
            reserved_map[row].add(seat)

        result = 2 * n

        for row, reserved in reserved_map.items():
            groups = 2
            block1 = all(seat not in reserved for seat in range(2, 6))
            block2 = all(seat not in reserved for seat in range(6, 10))

            if block1 and block2:
                continue
            elif block1 or block2:
                groups = 1
            else:
                block_mid = all(seat not in reserved for seat in range(4, 8))
                groups = 1 if block_mid else 0
            result -= (2 - groups)

        return result
        