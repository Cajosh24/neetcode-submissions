class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            match char:
                case "(": #opening brackets (add to stack)
                    stack.append("(")
                case "{":
                    stack.append("{")
                case "[":
                    stack.append("[")
                case ")": #closing brackets (check if stack has matching bracket or empty)
                    if len(stack) == 0:
                        return False
                    elif stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                case "}":
                    if len(stack) == 0:
                        return False
                    elif stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
                case "]":
                    if len(stack) == 0:
                        return False
                    elif stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
            
        return len(stack) == 0