class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        islands = 0
        rows, col = len(grid), len(grid[0])

        visit =  set()

        def bfs (r, c):

            q =  collections.deque()
            q.append((r,c))
            visit.add((r,c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                R, C = q.popleft()

                for dr, dc in directions:
                    if (R+dr) in range(rows) and (C+dc) in range(col) \
                    and grid[R+dr][C+dc] == '1' \
                    and (R+dr, C+dc) not in visit:
                        q.append((R+dr, C+dc))
                        visit.add((R+dr, C+dc))
        for r in range(rows):
            for c in range(col):
                if grid[r][c] == '1'and (r,c) not in visit:
                    bfs(r, c)
                    islands += 1
                

        return islands
        








        