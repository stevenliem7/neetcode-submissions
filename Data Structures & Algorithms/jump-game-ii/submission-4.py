class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for j in range(l , r+1):
                farthest = max(farthest, j + nums[j])
            jumps+=1
            l= r + 1 # l = index of farthest
            r=farthest
        return jumps