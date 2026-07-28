class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_freq = {}
        for char in s1:
            s1_freq[char] = s1_freq.get(char,0) + 1

        for i in range(len(s2) - len(s1) + 1):
            if s2[i] not in s1: #check if current char from s2 is in s1, if not then continue
                continue

            #check freq hash for each segment if match to s1 freq
            temp_freq = {}
            for j in range(i, i+len(s1)):
                temp_freq[s2[j]] = temp_freq.get(s2[j],0) + 1

            if temp_freq == s1_freq:
                return True
        
        return False
