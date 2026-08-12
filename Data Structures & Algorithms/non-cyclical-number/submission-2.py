class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        iter = n

        while True:
            
            sum = 0 #create new sum and iterate through number to add up sum
            while iter > 0:
                sum += pow(iter % 10, 2)
                iter = iter // 10 #increment through digits
            
            #check if sum 1 (non-cyclic), then in seen(cyclic), else add to set
            if sum == 1: return True
            elif sum in seen: return False
            else: seen.add(sum)

            iter = sum

        
        return False