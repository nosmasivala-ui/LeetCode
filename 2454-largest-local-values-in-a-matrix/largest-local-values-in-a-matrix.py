class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = n - 2
        ans = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                mx = grid[i][j]
                for di in range(3):
                    for dj in range(3):
                        mx = max(mx, grid[i+di][j+dj])
                ans[i][j] = mx
        return ans