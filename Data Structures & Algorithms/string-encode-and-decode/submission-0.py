class Solution:

    def encode(self, strs: List[str]) -> str:
        res_str=''
        for s in strs:
            res_str+=str(len(s))+'#'+s
        return res_str

    def decode(self, s: str) -> List[str]:
        word = ''
        res, i = [],0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            l = int(s[i:j])
            word = s[j+1:j+l+1]
            res.append(word)
            i=j+l+1
        return res
            
        # return s.split('#')
