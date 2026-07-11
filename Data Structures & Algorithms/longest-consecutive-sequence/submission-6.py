class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        curr_longest = 0
        for num in nums_set:

            if num-1 not in nums_set: # means this is a start of sequence
                curr_elem = num
                while curr_elem in nums_set:
                    curr_elem+=1
                    curr_longest+=1
                
                longest = max(longest, curr_longest)
                curr_longest = 0

        return longest