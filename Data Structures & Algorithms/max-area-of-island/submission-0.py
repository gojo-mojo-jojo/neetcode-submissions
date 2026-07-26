class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        max_area = 0
        rows, col = len(grid), len(grid[0])

        visited = set()
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r,c):
            
            count = 1
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))


            while q:
                R, C = q.popleft()

                for dr, dc in directions:
                    nr = R + dr
                    nc = C + dc

                    if nr in range(rows) and nc in range(col) and grid[nr][nc] == 1 and \
                    (nr, nc) not in visited:
                        count += 1
                        q.append((nr, nc))
                        visited.add((nr, nc))
            

            return count
        for r in range(rows):
            for c in range(col):
                if grid[r][c] == 1 and (r,c) not in visited:
                    num_nodes = bfs(r,c)
                    max_area = max(max_area, num_nodes)

    
        return max_area



                





