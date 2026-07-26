class Solution:
    def search(self, nums: List[int], target: int) -> int:

        mid = len(nums)//2

        def find_target(start, end):
            
            if start > end:
                return -1

            mid = (start + end)//2
            if nums[mid] == target:
                return mid

        
            if nums[mid] > target :
                return find_target(start, mid-1)
            
            else :
                return find_target(mid+1, end)

        return find_target(0, len(nums)-1)
        