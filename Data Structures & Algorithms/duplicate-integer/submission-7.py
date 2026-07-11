class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # { 1: 1,   2: 1,  3: 2}
        mapp = {}
        for i in nums:
            if i not in mapp:
                mapp[i] = 1000
            else:
                return True
        return False
        