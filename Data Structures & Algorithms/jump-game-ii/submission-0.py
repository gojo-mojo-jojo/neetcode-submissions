class Solution:
    def jump(self, nums: List[int]) -> int:
        L = R = 0

        count = 0
        while R < len(nums) - 1:
            far = 0
            for i in range(L, R+1):
                far = max(far, i+nums[i])
            L = R+1
            R = far
            count += 1
        return count





        