class Solution:
    def climbStairs(self, n: int) -> int:
        # Subproblem: The min number of steps taken up to point i of the staircase
        # Recurrence: OPT(i) = OPT(i-1) + OPT(i-2)
        cache = {}

        def helper(n):
            if n in cache:
                return cache[n]
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            cache[n] = helper(n - 1) + helper(n - 2)
            return cache[n]

        return helper(n)
                
