class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []

        for n in range(len(nums)-k+1):

            max_num = max(nums[n:n+k])
            res.append(max_num)
        return res
        