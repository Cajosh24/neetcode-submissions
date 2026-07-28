class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        
        for token in tokens:
            match token: #if operation, take stack inputs and use operation
                case "+":
                    num2 = numbers.pop()
                    num1 = numbers.pop()
                    numbers.append(num1 + num2)
                case "-":
                    num2 = numbers.pop()
                    num1 = numbers.pop()
                    numbers.append(num1 - num2)
                case "*":
                    num2 = numbers.pop()
                    num1 = numbers.pop()
                    numbers.append(num1 * num2)
                case "/":
                    num2 = numbers.pop()
                    num1 = numbers.pop()
                    numbers.append(int(num1 / num2))
                case _: #add number to stack
                    numbers.append(int(token))
        
        return numbers[0]

