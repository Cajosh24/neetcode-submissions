class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0

        best_length = 0

        for i, char in enumerate(s):
            #no repeat oounting from same streak
            if not i == 0 and s[i-1] == s[i]:
                continue

            j = i 
            limit = 0
            current_length = 0
            
            #incrment j as far as possible
            while limit <= k and j < len(s):
                if s[j] != char: #if not matching char, increment limit until k reached or end of string
                    limit += 1

                    if limit == k + 1:
                        continue

                #add current char to streak
                current_length += 1
                
                j += 1
            
            #decrement i as far as possible
            i -= 1
            while limit <= k and i >= 0:
                if s[i] != char: #if not matching char, decrement limit until k reached or end of string
                    limit += 1

                    if limit == k + 1:
                        continue

                #add current char to streak
                current_length += 1
                
                i -= 1

            #compare streak
            best_length = max(best_length,current_length)
        
        return best_length
            