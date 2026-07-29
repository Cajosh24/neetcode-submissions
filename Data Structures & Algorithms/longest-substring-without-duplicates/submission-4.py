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
            else: #resolve duplicate
                while not s[l] == s[r]:
                    seen.remove(s[l])
                    l += 1
                    current_length -= 1

                l += 1

            best_length = max(best_length,current_length)
            
            #increment right index
            r += 1

        return best_length


