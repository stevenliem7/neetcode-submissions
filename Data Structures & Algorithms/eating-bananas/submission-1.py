import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) # upper bound of eating rate is the max of piles
        best_rate = 0
        while l <= r:
            mid = l + (r - l) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h: # curr rate is fast enough, search left side if we can get faster 
                r = mid - 1
                best_rate = mid
            else:           # curr rate too slow, search right side
                l = mid + 1 

        return best_rate
        

        