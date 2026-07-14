class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        unique_freq = {}

        for i, string in enumerate(strs):

            freq = {}

            #get char frequency of current string
            for char in string:
                freq[char] = freq.get(char,0) + 1

        
            #add string to index of its matching freq
            if str(sorted(freq.items())) not in unique_freq:
                unique_freq[str(sorted(freq.items()))] = []
        
            unique_freq[str(sorted(freq.items()))].append(string)
            
        
        return list(unique_freq.values())
        
            

        