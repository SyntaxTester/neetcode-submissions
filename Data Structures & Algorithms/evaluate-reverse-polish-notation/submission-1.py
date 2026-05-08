from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        stack = self.RPN(tokens, stack)
        return stack[0]  # в конце в стеке остаётся одно число

    def RPN(self, tokens: List[str], stack: List[int]):
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token not in operators:
                # добавляем числа в стек
                stack.append(int(token))
            else:
                # достаём два последних числа
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    # для деления в Python нужно делать int(a / b), чтобы поведение как в RPN
                    stack.append(int(a / b))
        
        return stack