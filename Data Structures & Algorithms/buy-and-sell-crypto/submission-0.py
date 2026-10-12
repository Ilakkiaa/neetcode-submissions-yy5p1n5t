class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        res=0
        for i in prices:
            mini=min(mini,i)
            profit=i-mini
            res=max(res,profit)
        return res