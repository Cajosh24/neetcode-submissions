class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = len(board), len(board[0])

        filled_row = defaultdict()
        filled_col = defaultdict()
        filled_box = defaultdict()

        for i in range(rows):
            for j in range(cols):
                #check for non-blank box
                if board[i][j] != ".":
                    #get row, col, and box data combined with number to create unique data/val ID string
                    row_val = str(i) + "," + str(board[i][j])
                    col_val = str(j) + "," + str(board[i][j])
                    box_val = str(int(i/3) * 3 + int(j/3)) + "," + str(board[i][j])
                    
                    #check if number alr exist in any of 3 categories
                    if filled_row.get(row_val) == 1 or filled_col.get(col_val) == 1 or filled_box.get(box_val) == 1:
                        return False
                        
                    #record row, col, and box data
                    filled_row[row_val] = 1
                    filled_col[col_val] = 1
                    filled_box[box_val] = 1

                    print(row_val, col_val, box_val)
                
        return True