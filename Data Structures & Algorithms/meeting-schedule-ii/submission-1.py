"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_list = [i.start for i in intervals]
        end_list = [j.end for j in intervals]
        start_list.sort()
        end_list.sort()
        s,e = 0,0
        res,count = 0,0
        # print (len(end_list))
        while s<len(intervals) and e<len(intervals):
            # print ("Start",start_list[s])
            # print ("end",end_list[e])
            if start_list[s]<end_list[e]:
                s+=1
                count+=1
            else:
                e+=1
                count-=1
            res = max(count,res)
        return res




#         1,2 3,4 2,5 3,7 -->  1,2 3,4 
#                         --> 2,5 
#                         --> 3,7
# Basically we want the number of intersections amongst intervals. 
# Wider the intersection more the days
# 1) Pan out numbers in the interval, find intersection
# 2) 

        