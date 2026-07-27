class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        for char in s: 
            if char in match: #check stack for matching bracket if closed bracket
                if len(stack) != 0 and match[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else: #append to stack if open bracket
                stack.append(char)
            
        return len(stack) == 0