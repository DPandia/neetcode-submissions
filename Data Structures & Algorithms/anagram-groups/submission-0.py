class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list) #Initializes each k-v pair with value as empty array
        for x in strs:
            count = [0]*26
            for c in x:
                count[ord(c)-ord("a")]+=1
            hm[tuple(count)].append(x)
        # for x in strs:
        return list(hm.values())

