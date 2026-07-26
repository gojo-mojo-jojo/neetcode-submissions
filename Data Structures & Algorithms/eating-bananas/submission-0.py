class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        min_k = 1
        max_k = max(piles)

        L = min_k
        R = max_k

        res = 0 # float('inf')
        while L <= R:

            mid = (L + R) // 2
            total_time_pile = 0
            for i in range(len(piles)):
                rate = mid
                time_each_pile = math.ceil(piles[i]/rate)
                total_time_pile += time_each_pile
            if total_time_pile <= h:
                res = mid #min(res, mid)
                R = mid-1
            else:
                L = mid+1
        

        return res







        