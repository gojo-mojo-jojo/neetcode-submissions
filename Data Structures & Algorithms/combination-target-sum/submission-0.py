class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []

        def backtrack (i, curr):
            if sum(curr) == target:
                return res.append(curr.copy())

            if i >= len(nums) or sum(curr) > target:
                return #res.append(curr.copy())

            

            curr.append(nums[i])
            backtrack(i, curr)
            curr.pop()
            backtrack(i+1, curr)

        backtrack(0, curr)
        return res

        


        