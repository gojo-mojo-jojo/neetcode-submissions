class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        land = INF
        water = -1 
        treasure = 0

        rows = len(grid)
        col = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs (lr, lc):
            step = 0
            visited = set()
            q = collections.deque()
            q.append((lr, lc, step))
            visited.add((lr, lc))
            
            while q:
                qr, qc, curr_step = q.popleft()
                for dr, dc in directions:
                    nr = qr + dr
                    nc = qc + dc
                    
                    if nr in range(rows) \
                    and nc in range(col) \
                    and (nr, nc) not in visited \
                    and grid[nr][nc] != water:

                        nstep = curr_step + 1 
                        if grid[nr][nc] > treasure: #land is > 0 
                            #curr_step += 1
                            q.append((nr, nc, nstep))
                            visited.add((nr, nc))
                        else: #treasure
                            return nstep

            return grid[lr][lc]

        for r in range(rows):
            for c in range(col):
                if grid[r][c] == land:
                    grid[r][c] = bfs(r, c)


       