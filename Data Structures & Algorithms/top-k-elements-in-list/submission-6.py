import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = {i:[] for i in range(len(nums) + 1)}
        mapp = {}
        print(mapp)
        sol = []
        
        for num in nums:
            if num in mapp: mapp[num] += 1
            else: mapp[num] = 1
        
        for key,v in mapp.items():
            heap[v].append(key)
        print(heap)

        for i in range(len(heap) - 1, 0, -1):
            if len(sol) == k:
                return sol
            temp_val = heap.get(i)
        
            if temp_val is not None:
                # extend() unpacks the list [1, 2] into 1, 2
                # We also slice it [:k - len(sol)] to ensure we NEVER exceed k elements
                sol.extend(temp_val[:k - len(sol)])
        
        return sol
            
        


        