####### FileName=PlusOne.py


'''Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.'''


class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        amount = 1
        for i in range(len(digits)-1,-1,-1):
            if digits[i] + amount == 10:
                digits[i] = 0
                amount = 1
            else:
                digits[i] = digits[i] + amount
                amount = 0
        if i == 0 and amount ==1:
            digits.insert(0,1)
        return digits
