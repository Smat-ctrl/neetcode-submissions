class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            op = tokens[i]
            if op == "+" or op =="-" or op == "/" or op == "*":
                value1 = int(stack.pop())
                value2 = int(stack.pop())
                
                if op == "+":
                    stack.append(value2 + value1)
                if op == "-":
                    stack.append(value2 - value1)
                if op == "/":
                    stack.append(int(value2 / value1))
                if op == "*":
                    stack.append(value2 * value1)
                continue
            stack.append(int(op))
        
        return stack.pop()
