class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        rows, cols =  len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        cache = {}
        def dfs (r, c, prev_val):

            if r not in range(rows) or c not in range(cols):
                return 0 #float('-inf') #wrong path
        
            curr_val = matrix[r][c]
            if curr_val <= prev_val:
                return float('-inf')
            
            if (r,c) in cache:
                return cache[(r,c)]

            max_len = 1
            for (dr, dc) in directions:
                max_len = max(max_len, 1 + dfs(r+dr, c+dc, curr_val))
            
            cache[(r,c)] = max_len
            return max_len

        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c, float('-inf')))
        return ans



        
        