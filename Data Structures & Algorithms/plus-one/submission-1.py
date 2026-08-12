class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            if digits[-1 - i] != 9: #if not 9, safely add 1 then return
                digits[-1 - i] += 1
                return digits
            else:
                digits[-1 - i] = 0 #replace 9 with 0 then continue incrementing
        
        return [1] + digits