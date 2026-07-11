class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Keep the seen index number in set
        seen = set(())
        for row in range(9):
            for col in range(9):
                num = board[row][col]

                if num == ".":
                    continue

                col_key = col  # 0-8, one ID per column
                row_key = row + 9   # 9-17, one ID per row  
                box_key = (row // 3) * 3 + (col // 3) + 18  # 18-26, one ID per box

                if (col_key, int(num)) in seen or (row_key, int(num)) in seen or (box_key, int(num)) in seen:
                    return False
                
                seen.add((col_key, int(num) ))
                seen.add((row_key, int(num) ))
                seen.add((box_key, int(num) ))

        return True
            



        