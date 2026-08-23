class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total1 = 0
        for i, num in enumerate(reversed(num1)):
            total1 += (ord(num) - 48) * pow(10,i)

        total2 = 0
        for i, num in enumerate(reversed(num2)):
            total2 += (ord(num) - 48) * pow(10,i)

        return str(total1 * total2)
        