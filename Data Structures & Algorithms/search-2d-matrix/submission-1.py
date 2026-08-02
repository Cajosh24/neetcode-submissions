class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        start = (0,0)
        end = (m-1,n-1)

        #check if start 2d array index is less than/equal to end index
        while (n*start[0]+start[1] <= n*end[0]+end[1]):
            #1d array index
            mid = int((n*start[0]+start[1] + n*end[0]+end[1]) / 2)
            #2d array value
            mid_num = matrix[mid // n][mid % n]

            if mid_num > target:
                end = ((mid-1) // n, (mid - 1) % n) #convert to 2d index
            elif mid_num < target:
                start = ((mid +1 ) // n, (mid + 1) % n) #convert to 2d index
            else: return True #target found

        return False