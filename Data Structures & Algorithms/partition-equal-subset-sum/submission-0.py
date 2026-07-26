class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        target = total_sum/2
        cache = {}

        def helper (i, curr_sum):
            if i == len(nums):
                return False

            if curr_sum == target:
                return True

            if (i, curr_sum) in cache:
                return cache[(i, curr_sum)]

            skip = helper(i+1, curr_sum)
            add = helper(i+1, curr_sum+nums[i])
            
            cache[(i, curr_sum)] = skip or add
            return skip or add

        return helper(0, 0)
        