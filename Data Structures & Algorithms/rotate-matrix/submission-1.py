class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        switch = len(matrix) // 2 #number of rotations needed to occur
        
        for mod in range(switch):
            #mod to modify start position of rotation
            n = (len(matrix) - mod*2) - 1 #change size of rotation
            
            for i in range(n):
                temp_element = matrix[0 + mod][i + mod]
                matrix[0 + mod][i + mod] = matrix[n - i + mod][0 + mod]
                matrix[n - i + mod][0 + mod] = matrix[n + mod][n - i + mod]
                matrix[n + mod][n - i + mod] = matrix[i + mod][n + mod]
                matrix[i + mod][n + mod] = temp_element



            
        
        