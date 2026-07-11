class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_subarray = 0
        max_subarray = min(nums)
        for i in nums:
            # 2 conditions: If curr subarray <= 0, reset the sum, else continue
            curr_subarray += i
            # Check 1: is this run a new record? (always check)
            if curr_subarray > max_subarray:
                max_subarray = curr_subarray
              # Check 2: has the run gone negative? if so, abandon it
            if curr_subarray < 0:
                curr_subarray = 0
        
        return max_subarray