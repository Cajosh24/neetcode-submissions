class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Target = speed * time + position
        #Time = (target - position) / speed
        times = [0] * len(position)
        for i in range(len(position)):
            times[i] = (target - position[i]) / speed[i]

        cars = sorted(zip(position,times),reverse=True)
        fleets = 1
        curr_slowest = cars[0][1]

        for _,time in cars:
            if time > curr_slowest:
                fleets += 1
                curr_slowest = time
        
        return fleets

