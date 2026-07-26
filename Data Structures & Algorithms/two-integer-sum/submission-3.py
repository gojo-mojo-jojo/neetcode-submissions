class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #single pass for checking and adding to the dict
        lut = {}
    
        for i, num in enumerate(nums):
            diff = target - num
            if diff in lut:
                return [lut[diff], i]

            lut[num] = i
        return []

        