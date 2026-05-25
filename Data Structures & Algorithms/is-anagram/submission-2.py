class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        hm1={}
        hm2={}
        for x in s:
            hm1[x] = 1+hm1.get(x,0)
        for x in t:
            hm2[x] = 1+hm2.get(x,0)
        for x in hm1:
            if (hm1[x]!=hm2.get(x,0)):
                return False
        return True