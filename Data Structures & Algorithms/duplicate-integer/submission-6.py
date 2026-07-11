class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapp = {}
        for i in nums:
            if i in mapp:
                return True
            else:
                mapp[i] = 1
        return False
        