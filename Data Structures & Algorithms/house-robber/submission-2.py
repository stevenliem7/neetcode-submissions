class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        cache = [0] * n
        cache[0] = nums[0]
        cache[1] = max(nums[1], nums[0])
        
        # nums[0], nums[1], n, n+1, n+2
        for i in range(2, n):
            cache[i] = max(cache[i-2] + nums[i], cache[i-1])
        
        return max(cache)

        