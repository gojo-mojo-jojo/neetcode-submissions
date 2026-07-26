class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        if len(nums) == 1:
            return True

        goal_post = len(nums) - 1

        i = goal_post - 1
        while i >= 0:

            jump = nums[i] + i
            if jump >= goal_post:
                goal_post = i
            
            if goal_post == 0:
                return True

            i -= 1

        return False

