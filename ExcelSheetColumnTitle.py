###### FileName = ExcelSheetColumnTitle.py


'''Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA'
    28 -> AB '''

class Solution:
    # @return a string
    def convertToTitle(self, num):
        tail = ''
        while num:
            tail = chr(ord('A') + (num - 1) % 26) + tail
            num = (num - 1) // 26
        return tail
            
