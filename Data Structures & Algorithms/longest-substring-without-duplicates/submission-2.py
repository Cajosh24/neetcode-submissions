class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: 
            return 0

        seen = set()
        l = 0
        r = l
        best_length = 0
        current_length = 0

        while r < len(s):
            if s[r] not in seen: #add char to streak
                seen.add(s[r])
                current_length += 1
            elif s[l] == s[r]: #move sliding window
                l += 1
            else: #reset streak
                seen = set()
                seen.add(s[r])

                current_length = 1
                l = r

            best_length = max(best_length,current_length)
            
            #increment right index
            r += 1

        return best_length


