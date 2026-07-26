class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []

        for i in range(len(points)):
            distance = math.sqrt(points[i][0]**2 + points[i][1]**2)
            res.append([distance,[points[i][0], points[i][1]] ])

        
        res.sort()
        
        ans = [i[1] for i in res]
        return ans[:k]
        