class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2

            # if its increasing up to the midpoint, shift to right side, havent found the cut
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid
        
        return nums[l]




        