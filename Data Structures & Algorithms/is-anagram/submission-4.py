class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #return ((set(s) == set(t)) and (len(s) == len(t)))
        
        #same letters
        #same length
        #NOT same count of each letter
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for char in s:
            s_dict[char] += 1
        for char in t:
            t_dict[char] += 1

        return t_dict == s_dict