class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for x in strs:
            count = [0]*26
            for c in x:
                count[ord(c) - ord("a")]+=1
            hm[tuple(count)].append(x)
        return list(hm.values())

 
