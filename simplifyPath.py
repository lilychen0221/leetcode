###### FileName = simplifyPath.py

'''Given an absolute path for a file (Unix-style), simplify it.
For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".'''
'''[解题思路]
利用栈的特性，如果sub string element
1. 等于“/”，跳过，直接开始寻找下一个element
2. 等于“.”，什么都不需要干，直接开始寻找下一个element
3. 等于“..”，弹出栈顶元素，寻找下一个element
4. 等于其他，插入当前elemnt为新的栈顶，寻找下一个element

最后，再根据栈的内容，重新拼path。这样可以避免处理连续多个“/”的问题'''

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = []
        s="/"
        if path == "/../":
            return "/"
        for i in path:
            if i == "/":
                continue
            elif i == ".":
                continue
            elif i == ".." and stack != []:
                stack.pop()
            else:
                stack.append(i)
        for j in range(0, len(stack)):
            s + stack[j]
            s + "/"
        return s

