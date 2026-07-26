class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        def helper (i, M, N, cache):
            if i == len(strs):
                return 0

            if (i, M, N) in cache:
                return cache[(i, M, N)]
            #skip :
            skip  = helper(i+1, M, N, cache)

            #take
            take = 0
            zero =  strs[i].count('0')
            one =  strs[i].count('1')
            if zero <= M and one <= N:
             take = 1 + helper(i+1, M-zero, N-one, cache)


            cache[(i, M, N)] = max(take, skip)
            return cache[(i, M, N)]

        return helper(0, m, n, {})






        