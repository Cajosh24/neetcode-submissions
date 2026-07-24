class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        nums = sorted(nums)

        #adjust left/right pointers for each index
        for i in range(len(nums)):
            l = 0
            r = len(nums) - 1
            
            while l < r:
                #adjust left/right pointer to not overlap index i
                if l == i:
                    l += 1
                elif r == i:
                    r -= 1
                
                if l == r:
                    continue

                triplet = tuple(sorted([nums[l],nums[r],nums[i]]))
                
                #if combo works and not seen in res, add to res/seen
                if triplet not in seen and nums[l] + nums[r] + nums[i] == 0:
                    res.append(list(triplet))
                    seen.add(triplet)
                
                #decrement right if sum greater than 0, otherwise increment left
                if nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    l += 1

        return res



                


        