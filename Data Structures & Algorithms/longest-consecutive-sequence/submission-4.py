class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums)

        for num in nums:
            if num - 1 not in nums: # This num is the start of a sequence
                curr = num
                temp_longest=1
                while curr + 1 in nums:
                    temp_longest+=1
                    curr += 1
                longest = max(longest, temp_longest)
        return longest
