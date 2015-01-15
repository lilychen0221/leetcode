
###### Filename = RomanIntoInt.py 



class Solution:
    # @return a string
    def intToRoman(self, num):
        base = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        roman = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        result = ""
        for i in range(len(base)):
            while num >= base[i]:
                result = result + roman[i]
                num = num - base[i]
        return result 
