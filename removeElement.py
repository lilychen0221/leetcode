####### FileName = removeElement.py




'''https://oj.leetcode.com/problems/remove-element/'''

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
     def removeElement(self, A, elem):
        while A.count(elem):
            A.remove(elem)
        return len(A)
        
