from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])
            

        dp = [0] * len(nums)

        #i = 0
        dp[0], dp[1] = nums[0], max(nums[0],nums[1])

        i = 2
        while i < len(nums):

            dp[i] =  max(dp[i-1], nums[i]+dp[i-2])
            i += 1

        return dp[-1]



        # @lru_cache()
        # def dfs (i):

        #     if i >= len(nums):
        #         return 0

        #     skip = dfs(i+1)

        #     take = nums[i] + dfs(i+2)

        #     return max(skip, take)

        # return dfs(0)