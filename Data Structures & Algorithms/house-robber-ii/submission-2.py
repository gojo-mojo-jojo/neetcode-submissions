class Solution:
    def rob(self, nums: List[int]) -> int:

        def roblinear(nums):
            n = len(nums)
            memo = {}
            def dfs (i):

                if i >= n:
                    return 0
                if i in memo:
                    return memo[i]
                #skip this house
                rob, skip = 0, 0

                skip += dfs(i+1)
                #rob this house

                rob += nums[i] + dfs(i+2)

                memo[i] = max(skip, rob)

                return memo[i]
            
            return dfs(0)
        
        if len(nums) == 1:
            return nums[0]
        return max(roblinear(nums[:-1]), roblinear(nums[1:]))


        