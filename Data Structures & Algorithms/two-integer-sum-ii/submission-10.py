class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = set()

        for i in range(len(numbers)):
            for j in range(i,len(numbers)):
                if (i,j) not in seen:
                    
                    if numbers[i] + numbers[j] == target:
                        return [i+1,j+1]

                    seen.add((i,j))