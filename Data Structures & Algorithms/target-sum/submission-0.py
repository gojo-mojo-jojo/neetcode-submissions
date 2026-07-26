class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.helper(0, nums, target, 0, {})

    def helper(self, i, nums, target, total, cache):
        if i == len(nums) and target == total:
            return 1

        if i == len(nums):
            return 0

        if (i, total) in cache:
            return cache[(i,total)]
        
        count = 0

        count += self.helper(i+1, nums, target, total - nums[i],cache)

        count += self.helper(i+1, nums, target, total + nums[i], cache)

        cache[(i,total)] = count
        return count




        