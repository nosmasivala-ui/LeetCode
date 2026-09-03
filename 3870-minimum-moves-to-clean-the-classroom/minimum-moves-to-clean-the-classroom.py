class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter_positions = []
        start = None
        
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter_positions.append((i, j))
        
        litter_count = len(litter_positions)
        full_mask = (1 << litter_count) - 1
        
        litter_index = {pos: idx for idx, pos in enumerate(litter_positions)}
        q = deque([(start[0], start[1], 0, energy, 0)])
        bestEnergy = [[[ -1 for _ in range(1 << litter_count)] for _ in range(n)] for _ in range(m)]
        bestEnergy[start[0]][start[1]][0] = energy
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q:
            x, y, mask, e, steps = q.popleft()
            if mask == full_mask:
                return steps
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and classroom[nx][ny] != 'X':
                    ne = e - 1
                    if ne < 0:
                        continue
                    
                    new_mask = mask
                    if classroom[nx][ny] == 'L':
                        new_mask |= 1 << litter_index[(nx, ny)]
                    if classroom[nx][ny] == 'R':
                        ne = energy
                    
                    if ne > bestEnergy[nx][ny][new_mask]:
                        bestEnergy[nx][ny][new_mask] = ne
                        q.append((nx, ny, new_mask, ne, steps + 1))
        
        return -1
