########## FileName ==ValidParentheses.py

'''Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.'''
'''解题思路：判断括号匹配的合法性。使用一个栈来解决问题。
遇到左括号入栈，遇到右括号，检查栈顶的左括号是否匹配，如果匹配，弹栈，如果不匹配，返回错误。
如果栈为空，而遇到右括号，同样返回错误。遍历完后，栈如果不空，同样返回错误'''


class Solution:
    # @return a boolean
    def isValid(self, s):
        for i in s:
            if i == "(" or i == "[" or i =="{":
                stack.append(i)
                
            if i ==")":
                if stack==[] or stack.pop() != "(" : ###First stack == [] for exaple "]", no pop value
                    return False
            if i =="]":
                if  stack==[] or stack.pop() != "[" :  
                    return False
            if i =="}":
                if  stack==[] or stack.pop() != "{" : 
                    return False
        if len(stack)==0:
            return True
        else:
          return False
