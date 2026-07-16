class Solution:
    def trap(self, height: List[int]) -> int:
        containable = False
        sub_total = 0
        total = 0

        #count per layer/height method
        for level in range(1, max(height) + 1):
            for curr in height:
                #check if height is able to contain rain
                if curr >= level:
                    containable = True

                if containable:
                    
                    if curr < level: #add subtotal if non-block
                        sub_total += 1
                    else: #update subtotal if new block found to contain current rain
                        total += sub_total
                        sub_total = 0
            
            #reset stats on new layer
            containable = False
            sub_total = 0
        return total