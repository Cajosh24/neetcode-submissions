class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_freq = []
        unique_freq = []

        for i, string in enumerate(strs):

            freq = {}

            #get char frequency of current string
            for char in string:
                freq[char] = freq.get(char,0) + 1
            
            #all frequencies
            all_freq.append(freq)

            #all UNIQUE frequencies
            if freq not in unique_freq:
                unique_freq.append(freq)

        final = [[] for _ in range(len(unique_freq))]

        for i,freq in enumerate(all_freq):
            #use index of unique_freq for final list, arrange by index
            final[unique_freq.index(freq)].append(strs[i])
        
        return final





        



                