class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        
        stack_value = []
        stack_index = []

        for i in range(len(temperatures)):
            #clear stack of any shorter values to current and record distance in res
            while stack_value and stack_value[-1] < temperatures[i]:
                res[stack_index[-1]] = i - stack_index[-1]
                
                stack_value.pop()
                stack_index.pop()
            
            if not stack_value or stack_value[-1] >= temperatures[i]:
                stack_value.append(temperatures[i])
                stack_index.append(i)

        
        return res
        
        
            

        
            