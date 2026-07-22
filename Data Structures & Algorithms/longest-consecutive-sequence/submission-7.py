class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        best_seq = 1
        curr_seq = 1

        nums = set(nums)

        for num in nums:
            #check if beginning of sequence
            if num - 1 not in nums:
                
                while num + 1 in nums: #if start found, keep incrmementing for sequence length
                    curr_seq += 1
                    num += 1
                
                if curr_seq >= best_seq: #compare current and best sequence lengths
                    best_seq = curr_seq
                    curr_seq = 1
                
        return best_seq