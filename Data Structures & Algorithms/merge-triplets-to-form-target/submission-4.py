class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        x, y, z = False, False, False

        for t in triplets:

            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            if t[0] == target[0]:
                x = True
            if t[1] == target[1]:
                y = True
            if t[2] == target[2]:
                z = True
                
        return (x and y and z)







