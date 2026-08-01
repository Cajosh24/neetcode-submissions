class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        peak_height = max(height)

        if peak_height == 0:
            return 0
        
        peak_index = height.index(peak_height)

        #find left local minimmum
        l = 0

        while height[l] == 0:
            l += 1
        left_local_max = height[l]
        
        #keep iterating through l pointer until reach peak while counting water
        l += 1
        while l < peak_index:
            if left_local_max <= height[l]:
                left_local_max = height[l]
            else:
                total += left_local_max - height[l]
            l += 1

        
        #find right local minimum
        r = len(height) - 1

        while height[r] == 0:
            r -= 1
        right_local_max = height[r]
        
        #keep iterating through r pointer until reach peak while counting water
        while r > peak_index:
            if right_local_max <= height[r]:
                right_local_max = height[r]
            else:
                total += right_local_max - height[r]
            r -= 1

        return total

        