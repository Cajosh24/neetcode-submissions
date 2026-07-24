class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            #check if pair sums to target
            if numbers[l] + numbers[r] == target: 
                return [l+1,r+1]

            #decrease right if sum greater than target, otherwise increase left
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1