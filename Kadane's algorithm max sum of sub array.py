Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.
>>> #kadane's algorithm
>>> 
# Was in right approach and almost solved it but was resetting temp value everytime instead when it was negative. Had to look at Editorial after time limit.
##Complete this function
def maxSubArraySum(a,size):
    ##Your code here
    temp=0
    sum1=0
 
    for x in range(0,size):
        temp +=a[x]
        if ((temp)>sum1):
            sum1 = temp
            # Was right till here, Didn't reset temp value to 0 when it's negative was instead directly resetting to 0, understood this after looking in to Editorial.
        if temp<0:
            temp=0
    return sum1    
