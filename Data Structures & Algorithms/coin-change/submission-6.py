class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        cache = {}
        def dfs (curr_sum):
            

            if curr_sum > amount:
                return float('inf')

            if curr_sum == amount:
                return 0

            if curr_sum in cache:
                return cache[curr_sum]

            res = float('inf')
            for c  in coins:
                res = min(res, 1 + dfs(curr_sum + c))
            
            cache[curr_sum] = res 

            return res
        
        ans = dfs(0)
        
        return int(ans) if ans != float('inf') else -1   




        