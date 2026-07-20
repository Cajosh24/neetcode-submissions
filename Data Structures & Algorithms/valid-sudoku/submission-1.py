class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        filled_row = set()
        filled_col = set()
        filled_box = set()

        for i in range(rows):
            for j in range(cols):
                #check for non-blank box
                if board[i][j] != ".":
                    #get row, col, and box data combined with number to create unique data/val tuple
                    row_val = (i, board[i][j])
                    col_val = (j, board[i][j])
                    box_val = (int(i/3) * 3 + int(j/3), board[i][j])
                    
                    #check if number alr exist in any of 3 categories
                    if (row_val in filled_row) or (col_val in filled_col) or (box_val in filled_box):
                        return False
                        
                    #record row, col, and box data
                    filled_row.add(row_val)
                    filled_col.add(col_val)
                    filled_box.add(box_val)
                
        return True