class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        return str(strs)

    
    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        decoder = eval(s)

        return decoder
        


