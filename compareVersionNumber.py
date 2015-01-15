####### FileName = CompareVersionNumbers.py

'''Compare two version numbers version1 and version1.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37'''

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = version1.split(".")
        v2 = version2.split(".")
        len1 = len(v1)
        len2 = len(v2)
        maxlen = max(len1, len2)
        v1num = 0
        v2num = 0 
        for x in range(maxlen):
            if x < len1:
                v1num = int(v1[x])
            if x >= len1 and x < maxlen:
                v1num = 0
            if x < len2:
                v2num = int(v2[x])
            if x >= len2 and x < maxlen:
                v2num = 0
            if v1num < v2num:
                return -1
            if v1num > v2num:
                return 1
            if v1num == v2num:
                continue
        return 0



