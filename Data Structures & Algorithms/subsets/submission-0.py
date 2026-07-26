class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, curr = [], []
        self.helper(0, nums, res, curr)
        return res
    
    def helper(self, i:int, nums: List[int], res: List[int],curr: List[int]):

        if i >= len(nums):
            return res.append(curr.copy())

        curr.append(nums[i])
        self.helper(i+1, nums, res, curr)
        curr.pop()
        self.helper(i+1, nums, res, curr)

        