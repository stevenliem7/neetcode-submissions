class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}
        sol = []
        for num in nums:
            if num in mapp: mapp[num] += 1
            else: mapp[num] = 1
        sorted_mapp = sorted(mapp, key=mapp.get, reverse=True)

        for i in range(k):
            sol.append(sorted_mapp[i])

        return sol
        


        