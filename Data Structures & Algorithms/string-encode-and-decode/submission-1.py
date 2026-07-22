class Solution:

    def encode(self, strs: List[str]) -> str:
        encoder = ""
        for string in strs:
            encoder = encoder + str(len(string)) + "#" + string
        
        return encoder

    
    def decode(self, s: str) -> List[str]:
        decoder = []
        start_length = 0

        while start_length < len(s):
            end_length = start_length

            #check string until delimiter
            while s[end_length] != "#":
                end_length += 1
            
            #get total word length
            word_length = int(s[start_length:end_length])
            
            #use word length and endpoint to retrieve word
            decoder.append(s[end_length + 1:end_length + 1 + word_length])

            #update startpoint
            start_length = end_length + 1 + word_length
        
        return decoder



        

