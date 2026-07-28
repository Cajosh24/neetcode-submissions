class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        operation = {"+","-","*","/"}
        
        for token in tokens:
            if token in operation: #if operation, take stack inputs and use operation
                num2 = numbers.pop()
                num1 = numbers.pop()
                
                match token:
                    case "+":
                        numbers.append(num1 + num2)
                    case "-":
                        numbers.append(num1 - num2)
                    case "*":
                        numbers.append(num1 * num2)
                    case "/":
                        numbers.append(int(num1 / num2))
            else: #add number to stack
                numbers.append(int(token))
        
        return numbers[0]

