class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest=0
        for pos_start in nums:
            if pos_start-1 not in numset:
                start = pos_start
                length=0
                while start in numset:
                    start+=1
                    length+=1
                    longest=max(length,longest)
        return longest            


        