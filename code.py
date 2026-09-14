class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        n=len(nums)
        d={}
        for i in range(n-1):
            c=nums[i]
            ne=nums[i+1]
            if c==key:
                if ne not in d:
                    d[ne]=1
                else:
                    d[ne]+=1
        maxn=0
        print(d)
        for v in d.values():
            maxn=max(maxn,v)
        mxn=0
        for k,v in d.items():
            if v==maxn:
                mxn=max(mxn,k)
        return mxn

        
