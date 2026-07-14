class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {}
        for index, value in enumerate(nums):

            #check hash for index of complement to target
            if (target - value) in indices:
                if index > indices.get(target - value):
                    return [indices.get(target - value), index]
                else:
                    return [index, indices.get(target - value)]
            
            #add value-index to hash
            indices[value] = index
        
                