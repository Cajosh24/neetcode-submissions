class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        #make freq hash table
        for value in nums:
            freq[value] = freq.get(value,0) + 1
        
        #sort hash by asc freq
        freq = dict(sorted(freq.items(), key=lambda x: x[1],reverse=False))

        #find highest value, then pop (for k times)
        final = []
        for i in range(k):
            final.append(freq.popitem()[0])

        return final
        