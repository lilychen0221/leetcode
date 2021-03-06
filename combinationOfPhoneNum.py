######## Filename = LetterCombinationsofaPhoneNumber.py



class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        res = [ ]
        lenS = len(digits)
        
        def dfs(num, string, res):
            if num == lenS:
                res.append(string)
                return 
            for letter in dict[digits[num]]:
                dfs(num+1, string+letter, res)
                
        dict = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        
        dfs(0, '', res)
        return res