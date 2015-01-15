###### FileName = RomanToInt.py


'''Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.'''


'''RL = ["I", "V","L" "X", "C", "D", "M"]
   IL = [1, 5, 10, 50, 100, 500, 1000]'''

class Solution:
    # @return an integer
    def romanToInt(self, s):
        sum = []
        result = 0
        for item in s:
            if item == "I":
                ivalue = 1
                sum.append(ivalue)
            if item == "V":
                ivalue = 5
                sum.append(ivalue)
            if item == "X":
                ivalue = 10
                sum.append(ivalue)
            if item == "L":
                ivalue = 50
                sum.append(ivalue)
            if item == "C":
                ivalue = 100
                sum.append(ivalue)
            if item == "D":
                ivalue = 500
                sum.append(ivalue)
            if item == "M":
                ivalue = 1000
                sum.append(ivalue)
        for j in range(len(s)-1):
            if sum[j] >= sum[j+1]:
                result = result+sum[j]
            else:
                result = result-sum[j]
        result = result + sum[len(s)-1]
        return result
            
        
