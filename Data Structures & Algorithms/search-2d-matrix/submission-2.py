class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        start = 0
        end = (m * n) - 1

        while (start <= end):
            mid = (start + end) // 2
            mid_m = mid // n
            mid_n = mid % n

            if matrix[mid_m][mid_n] > target:
                end = mid - 1
            elif matrix[mid_m][mid_n] < target:
                start = mid + 1
            else: return True 

        return False