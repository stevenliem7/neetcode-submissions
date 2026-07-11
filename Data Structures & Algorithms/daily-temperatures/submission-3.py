class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = [] # stores elements in: (temp, idx)
        for idx, temp in enumerate(temperatures): 
            # pop stack and process, bcs we found a bigger temp
            while stack and temp > stack[-1][0]:
                elem = stack.pop()
                old_temp, old_idx = elem[0], elem[1]
                out[old_idx] = idx - old_idx
            stack.append((temp, idx))

        return out
        