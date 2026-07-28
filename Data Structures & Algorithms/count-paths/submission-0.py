class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        cache = {}
        visited = set()
        def dfs(r, c, path):
            if r >= m or c >= n:
                return 0

            if (r,c) in path:
                return 0

            

            if r == m-1 and c == n-1:
                return 1
            
            if (r,c) in cache:
                return cache[(r,c)]

            path.add((r,c))
            
            turn = 0
            turn  += dfs(r+1, c, path) #down
            turn  += dfs(r, c+1, path) #right
            
            path.remove((r,c))
            cache[(r,c)] = turn
            return turn
        
        res = 0

        # for r in range(m):
        #     for c in range(n):
        #         if (r,c) not in visited:
        #             res += dfs(r,c)
        res = dfs(0 , 0, visited)
        return res

        