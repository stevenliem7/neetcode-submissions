class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            # base case, if target is found, return:
            if nums[mid] == target:
                return mid
            
            # if target > mid, recurse on the right sub-array
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return -1

        