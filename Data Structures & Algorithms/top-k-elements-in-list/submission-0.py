class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        if len(nums)==1:
            return nums
        for i in nums:
            if i not in d:
                d[i]=1
            elif i in d:
                d[i]+=1
        res=sorted(d,key=lambda x:d[x],reverse=True)
        return res[:k]

        

        