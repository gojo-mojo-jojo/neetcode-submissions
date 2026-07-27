class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, col = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0, -1)]

        visited = set()
        count = 0
        def bfs(r, c):
            q = collections.deque()
            
            q.append((r,c))
            visited.add((r,c))


            while q:
                qr, qc = q.popleft()

                for dr, dc in directions:
                    nr = dr + qr
                    nc = dc + qc

                    if nr in range(rows) and nc in range(col) and grid[nr][nc] == '1' and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))

            return 1

        count = 0
        for r in range(rows):
            for c in range(col):
                if (r,c) not in visited and grid[r][c] == '1':
                    count += bfs(r, c)

        return count

