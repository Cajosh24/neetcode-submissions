class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_freq = {}
        i = 0
        j = i

        best_length = 0
        current_length = 0

        while j < len(s):
            #add newest char to freq hash
            s_freq[s[j]] = s_freq.get(s[j],0) + 1
            current_length += 1

            #resolve k
            while (((j-i)+1) - max(s_freq.values())) > k:
                s_freq[s[i]] = s_freq.get(s[i],0) - 1
                current_length -= 1
                i += 1

            #compare max length
            best_length = max(best_length,current_length)

            j += 1

        return best_length
            
            