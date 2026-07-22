class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        best_seq = 1
        curr_seq = 1

        #sorted/unique elements for easier checking
        nums = sorted(set(nums))

        for num in nums:
            if num + 1 in nums: #add to sequence if next element is +1
                curr_seq += 1
            else: #compare curr to best if curr_seq breaks
                if curr_seq >= best_seq:
                    best_seq = curr_seq
                    curr_seq = 1
        
        if curr_seq > best_seq:
            best_seq = curr_seq
            
        return best_seq

            


        
                


            
        




