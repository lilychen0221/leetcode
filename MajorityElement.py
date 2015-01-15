###### FileName = MajorityElement.py

'''Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

'''




class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        ME,count = None, 0
        for e in num:
            if count == 0:
                ME = e
                count = 1
            elif e == ME:
                count += 1
            else:
                count -= 1
        return ME
        
