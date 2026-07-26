class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:


        def helper(i, cache):

            if i == len(days):
                return 0
            if i in cache:
                return cache[i]
            #use pass1
            cost_0 = costs[0] + helper(i+1, cache)

            #use pass2
            j = i
            while j < len(days) and days[j] < days[i] + 7:
                j += 1 
            cost_1 = costs[1] + helper(j, cache)

            #use pass3
            j = i
            while j < len(days) and days[j] < days[i] + 30:
                j += 1 
            cost_2 = costs[2] + helper(j, cache)

            cache[i] = min(cost_0, cost_1, cost_2)

            return min(cost_0, cost_1, cost_2)
        return helper(0, {})
        