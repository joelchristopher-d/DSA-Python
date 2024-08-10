class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=sorted(s)
        t=sorted(t)
        i=0
        while len(s)>i and len(t)>i:
            # print(t[i],s[i])
            if t[i]!=s[i]:
                return t[i]
            i+=1
        return t[-1]
        
