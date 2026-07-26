class Solution:
    def rob(self, nums: List[int]) -> int:
        
        max_amount = 0
        cache = {}
        def backtrack(i):
            
            if i in cache:
                return cache[i]
            if i >= len(nums):
                return 0

            skip = backtrack(i+1)

            take =  nums[i] + backtrack(i+2)

            max_amount = max(take, skip)
            cache[i] = max_amount
            return max_amount
        return backtrack(0)
