class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        L = 0 
        R = len(numbers) - 1
        while L < R:
            
            curr_sum = numbers[L] + numbers[R]
            if curr_sum > target:
                R -= 1
            
            if curr_sum < target:
                L += 1

            if curr_sum == target:
                return [L+1, R+1]

        return []





        
