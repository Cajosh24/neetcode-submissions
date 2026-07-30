class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_freq = {}
        l = 0
        r = l

        best_length = 0

        while r < len(s):
            #add newest char to freq hash
            s_freq[s[r]] = s_freq.get(s[r],0) + 1

            #resolve k
            while (((r-l)+1) - max(s_freq.values())) > k:
                s_freq[s[l]] -= 1
                l += 1

            #compare max length
            best_length = max(best_length,(r-l)+1)

            r += 1

        return best_length
            
            