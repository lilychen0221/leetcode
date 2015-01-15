####### FileName == StringtoInteger.py

'''Implement atoi to convert a string to an integer.'''

class Solution:
    # @return an integer
    def atoi(self, str):
        if str =="":
            return 0  
            
        s = str.strip( )
        min =  -2147483648
        max = 2147483647
        sign= 1
        i = 0
        if s[0] == "+" :
            s = s[1:]
        elif s[0]=="-":
            sign =  -1
            s = s[1:]
        while i < len(s) and s[i].isdigit():
            i = i + 1
        if i != 0:
            s = s[0:i]
            result = int(s)
        else:
            result = 0
        result = sign * result
        if result < 0:
            if result < min:
                return min
            else:
                return result
        if result > 0:
            if result > max:
                return max
            else:
                return result
