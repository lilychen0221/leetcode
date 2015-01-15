######### FileName = ReversePolishNotation.py

'''Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
逆波兰表达式的解释器一般是基于堆栈的。解释过程一般是：操作数入栈；遇到操作符时，操作数出栈，求值，将结果入栈；
当一遍后，栈顶就是表达式的值。因此逆波兰表达式的求值使用堆栈结构很容易实现，和能很快求值。'''

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i not in ('+', '-', '*', '/'):
                stack.append(int(i))
            else:
                s2 = stack.pop()
                s1 = stack.pop()
                if i == '+': stack.append(s1 + s2)
                elif i == '-': stack.append(s1 - s2)
                elif i == '*': stack.append(s1 * s2)
                else: stack.append(int(s1 * 1.0 / s2))
        return stack[0]
