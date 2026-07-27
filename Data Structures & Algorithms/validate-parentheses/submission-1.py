class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        for char in s: #append to stack if open bracket
            if(char == "(" or char == "{" or char == "["):
                stack.append(char)
            else: #check stack for matching bracket if closed bracket
                if len(stack) == 0:
                    return False
                
                if match[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
        return len(stack) == 0