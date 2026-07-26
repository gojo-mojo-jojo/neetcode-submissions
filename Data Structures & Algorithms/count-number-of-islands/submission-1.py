class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        island = set() # set of r,c


        count = 0 

        rows = len(grid)
        col = len(grid[0])

        def bfs (lr, lc):
            nonlocal count
            count += 1
            q = collections.deque()
            q.append((lr,lc))
            island.add((lr,lc))
            while q:
                qr, qc  = q.popleft()
                for dr, dc in directions: 
                    nr = qr + dr
                    nc = qc + dc
                    if nr in range(rows) \
                    and nc in range(col) \
                    and (nr, nc) not in island \
                    and grid[nr][nc] == '1':
                        island.add((nr,nc))
                        q.append((nr, nc))
                




        for r in range(rows):
            for c in range(col):

                if (r,c) in island or grid[r][c] == '0':
                    continue
                bfs(r,c)
               

                
        return count