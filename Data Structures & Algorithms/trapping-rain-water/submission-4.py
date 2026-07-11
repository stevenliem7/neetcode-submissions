class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        area = 0
        while l < r:

            if maxL < maxR:
                area+= max(0, maxL - height[l])
                l+=1
                maxL = max(maxL, height[l])
            else:
                area+= max(0, maxR - height[r])             
                r-=1
                maxR = max(maxR, height[r])  
        
        return area

            
        