class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = 0

        #get total (excluding zero) and zero count
        for num in nums:
            if num != 0:
                total *= num
            else:
                zero_count += 1
        
        #logic: 
        #2+ zeros: total always zero
        #1 zeros: total zero except without zero, else total/num
        #0 zeros: divide total/num 
        final = []
        for num in nums:
            if zero_count >= 2:
                final.append(0)
            elif zero_count == 1:
                if num == 0:
                    final.append(total)
                else:
                    final.append(0)
            else:
                final.append(int(total/num))

        return final
            