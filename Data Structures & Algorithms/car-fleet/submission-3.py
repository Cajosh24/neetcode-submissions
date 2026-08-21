class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Target = speed * time + position
        #Time = (target - position) / speed
        for i in range(len(position)):
            speed[i] = (target - position[i]) / speed[i]

        arr = sorted(zip(position,speed))
        fleets = 0
        stack = []

        for i in range(len(position)):
            current_time = arr[i][1]
            fleets += 1
            
            while stack and current_time >= stack[-1]:
                stack.pop()
                fleets -= 1
            
            stack.append(current_time)
        
        return fleets

