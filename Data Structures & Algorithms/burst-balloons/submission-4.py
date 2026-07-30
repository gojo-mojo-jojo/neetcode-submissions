from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #Interval DP (use interval state (l,r))


        nums = [1] + nums + [1]
        dp = {}
        @cache
        def dfs(l, r):

            if l + 1 >= r:
                return 0
            
            if (l, r) in dp:
                return dp[(l,r)]

            best = 0
            for i in range(l+1, r):

                coins = nums[l] * nums[i] * nums[r] #its the last one so 1*nums[i]*1 = nums[i]
                coins += dfs(l,i) + dfs(i, r)
                best = max(best, coins)
            
            dp[(l,r)] = best
            return dp[(l,r)] 
        
        return dfs(0, len(nums)-1)
        