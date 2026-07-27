class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        lut = {}
        for i, n in enumerate(nums):

            if n not in lut:
                lut[n] = i
            else:
                j = lut[n] 
                if abs(i-j) <= k:
                    return True
                lut[n] = i
        
        return False