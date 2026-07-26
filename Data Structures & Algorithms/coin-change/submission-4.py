class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def helper(i, rem_amount, cache):
            if i >= len(coins):
                return float('inf')
            if rem_amount == 0:
                return 0
            if (i, rem_amount) in cache:
                return cache[(i, rem_amount)]
            #skip
            skip = helper(i+1, rem_amount, cache)

            take = float('inf')
            new_rem = rem_amount - coins[i]
            if new_rem >= 0:
                take = 1 + helper(i, new_rem, cache)
            
            cache[(i, rem_amount)] = min(skip, take)

            return min(skip, take)

        res = helper(0, amount, {})
        return -1 if res == float('inf') else res
            




        