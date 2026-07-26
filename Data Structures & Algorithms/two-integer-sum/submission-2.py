class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #convert the list to set
        lut = {num:i for i,num in enumerate(nums)}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in lut and lut[diff] != i:
                return [i, lut[diff]]
        
        return []

        