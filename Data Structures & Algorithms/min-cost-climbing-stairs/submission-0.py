class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        curr = 0
        if n == 1:
            return cost[0]
        if n == 2:
            return min(cost[0], cost[1])
        
        cache = [0] * n
        cache[0] = cost[0]
        cache[1] = cost[1]

        for i in range(2,n):
            cache[i] = cost[i] + min(cache[i-1], cache[i-2])
        
        return min(cache[n-1], cache[n-2])
