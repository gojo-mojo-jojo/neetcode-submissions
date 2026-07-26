class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        min_win = float('inf')
        L = 0

        for R in range(len(nums)):
            sum += nums[R] 

            while sum >= target:
                min_win = min(min_win, R-L+1)
                sum -= nums[L]
                L += 1

        return 0 if min_win == float('inf') else min_win











        