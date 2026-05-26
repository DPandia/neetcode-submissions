class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i in range(0,len(nums)):
            ele = nums[i]
            
        # for i in range(0,len(nums)):
        #     ele = nums[i]
            complement = target - ele
            if complement in hm:
                ind = hm.get(complement)
                # print("HI")
                return ([min(i,ind),max(i,ind)])
            hm[ele] = i

                





        