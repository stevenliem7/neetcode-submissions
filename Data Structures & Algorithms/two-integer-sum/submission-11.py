class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}
        for i in range(len(nums)):
            if nums[i] in diffs.keys():
                return [diffs.get(nums[i]), i]
            diff = target - nums[i]
            diffs[diff] = i