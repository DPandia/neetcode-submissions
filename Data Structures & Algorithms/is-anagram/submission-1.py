class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        hm1 = {}
        hm2 = {}
        for x in s:
            hm1[x] = 1+hm1.get(x,0)
        for y in t:
            hm2[y] = 1+hm2.get(y,0)
        for z in s:
            if hm1[z]!=hm2.get(z,0):
                return False
        return True

        