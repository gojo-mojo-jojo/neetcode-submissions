class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def fib(n):
            if n in memo:
                return memo[n]
            if n < 2:
                return 1
            
            memo[n] = fib(n-1) + fib(n-2)
            return memo[n]

        return fib(n)
