# Best Time to Buy and Sell Stock
#initial Brute force approach I did
#Time comp O(n2) and breached time limit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        pro=0
        for x in range(len(prices)):
            for y in range(x,len(prices)):
                if(prices[y]>prices[x]):
                    pro =prices[y]-prices[x]
                    if(pro>maxp):
                        maxp=pro
                    
        return maxpro








#Best appraoch with time comp O(n) with only one for loop, learnt from editorial
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        minp=sys.maxsize
        for x in range(len(prices)):
            if(prices[x]<minp):
                minp=prices[x]
            elif(prices[x]-minp >maxp):
                maxp = prices[x]-minp
                    
        return maxp
                    
                    
        
