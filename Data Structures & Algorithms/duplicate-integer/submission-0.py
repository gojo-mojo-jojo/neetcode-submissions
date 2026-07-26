class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lut = set()
        for n in nums:
            if n in lut:
                return True
            lut.add(n)
        return False
        