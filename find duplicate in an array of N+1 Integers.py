Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #find duplicate in an array of N+1 Integers
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr=[]
        for x in nums:
            if x not in arr:
                arr.append(x)
            else:
                return x
        