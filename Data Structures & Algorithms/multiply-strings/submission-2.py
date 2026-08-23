class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total = 0
        for i, top_num in enumerate(reversed(num1)):
            curr = 0
            for j, bot_num in enumerate(reversed(num2)):
                curr += (ord(top_num) - 48) * (ord(bot_num) - 48) * (10 ** j)
        
            total += curr * (10 ** i)
        

        return str(total)
        