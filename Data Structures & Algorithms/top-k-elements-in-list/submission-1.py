class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            my_dict[num] = my_dict.get(num, 0) + 1
    
        sorted_list = sorted(my_dict, key=my_dict.get, reverse=True)

        return sorted_list[:k]


        