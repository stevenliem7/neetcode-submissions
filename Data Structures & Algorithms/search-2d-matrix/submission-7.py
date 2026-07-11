class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # if target = less than the last element of the column,
        # perform binary search on both the rows and columns

        # Process columns first
        right = len(matrix[0]) - 1
        mid = 0

        for row in matrix:
            top = 0
            bottom = len(matrix) - 1
            while top <= bottom:
                mid = top + (bottom - top) // 2
                if target >= matrix[mid][0] and target <= matrix[mid][right]: # found the correct strip
                    break
                elif target > matrix[mid][0]:
                    top = mid + 1
                else:
                    bottom = mid - 1

        # process the individual strip / row   
        left = 0
        while left <= right:
            middle = left + (right - left) // 2
            if matrix[mid][middle] == target:
                return True
            elif target > matrix[mid][middle]:
                left = middle + 1
            else:
                right = middle - 1
        
        return False





