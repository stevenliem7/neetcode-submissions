class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0
        for idx, height in enumerate(heights):
            start = idx
            # the idea is to continuously pop elements tht are bigger than curr
            while stk and stk[-1][1] > height:
                temp_idx, temp_height = stk.pop()
                max_area = max(max_area, temp_height * (idx - temp_idx))
                start = temp_idx

            # we append the idx of the max width this element can cover
            stk.append((start, height))

        # another sweep to clean the monotonic stack
        hist_height = len(heights)
        for height in stk:
            max_area = max(max_area, height[1] * (hist_height - height[0]))

        return max_area