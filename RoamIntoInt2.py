
##### Filename = RoamIntoInt2.py
''' Using dictionary rather than list to store the roman and integer''''


class Solution:
    # @return an integer
    def romanToInt(self, s):
        result = 0
        numerals = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        last = 0
        result = 0
      
        for x in s:
             if last and last >= numerals[x]:
                result += last
                last = numerals[x]
             else:
                   result -= last
                   last = numerals[x]
        result += numerals[x]    
        return result



 ####### Only function           
def romanToInt(s):
        result = 0
        numerals = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        last = 0
        result = 0
      
        for x in s:
             if last and last >= numerals[x]:
                result += last
                last = numerals[x]
                print("last, result is", last, result)
             else:
                   result -= last
                   last = numerals[x]
                   print("last, result is", last, result)                  
        result += numerals[x]          
        print(result)
        return result


print(romanToInt("DCXXI"))
