class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        if len(piles) > h:
            return False

        def condition_met(rate):
            
            t = 0
            for p in piles:
                t += p // rate
                if p % rate > 0:
                    t += 1
     
            if t > h:
                return False
            else:
                return True


        #do Binary search
        #range of values is min rate=  1, max rate = max value of banana

        L = 1
        R = max(piles) 
        ans  = 0
        while L <= R:

            mid = ((L + R) // 2) 

            if condition_met(mid):
                R = mid - 1
                ans = mid
            else :
                L = mid + 1

        return ans
