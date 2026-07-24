class Solution:
    def maxArea(self, heights: List[int]) -> int:
        highest_area = 0 
        i = 0
        j = len(heights) - 1

        while i < j:
            #calculate current are base on lowest height and compare to highest
            curr_area = min(heights[i], heights[j]) * (j - i)
            highest_area = max(highest_area,curr_area)
            
            #incrment/decrement smaller height
            if heights[i] >= heights[j]:
                j -= 1
            else:
                i += 1
            

        return highest_area
        