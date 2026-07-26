class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max =  1
        curr_min = 1
        res =  float('-inf')

        for n in nums:
            tmp = n*curr_max
            curr_max = max(n*curr_max, n*curr_min, n)
            curr_min = min(tmp, n*curr_min, n)
            res = max(res, curr_max)
        return int(res)



            


        