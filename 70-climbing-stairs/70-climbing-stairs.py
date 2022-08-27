# from functools import cache

class Solution:
    
    # @cache # cache for memoization
    def climbStairs(self, n: int, memo = None) -> int:
        # if we have 1 step left we can only climb that with one step
        # if we have 2 steps we can climb them in two ways (see example 1 in question)
        if n < 3:
            return n
        if memo is None :
            memo = {}
        if n in memo: return memo[n]
        memo[n] = self.climbStairs(n-1,memo) + self.climbStairs(n-2,memo)
        # at each step X we can either take 1 to 2 steps leaving the 
        # remaining number of steps to be either X - 1 or X - 2
        # depending on our choice

        return memo[n]