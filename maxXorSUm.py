class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt=0
        j=0
        for i in range(len(s)):
            if j+2>=len(s):
                break
            t=s[j:j+3]
            if len(list(t))==len(set(t)):
                cnt+=1
            j+=1
        return cnt

class Solution:
    def minPairSum(self, l: List[int]) -> int:
        l.sort()
        n=len(l)
        res=0
        for i in range(n//2):
            res=max(res,l[i]+l[n-1-i])
        return res
