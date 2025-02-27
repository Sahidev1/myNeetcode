
#You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents the start and the end time of the ith interval. 
#intervals is initially sorted in ascending order by start_i.
#
#You are given another interval newInterval = [start, end].
#
#Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and also intervals still does not have any overlapping intervals. 
#You may merge the overlapping intervals if needed.
#
#Return intervals after adding newInterval.
#
#Note: Intervals are non-overlapping if they have no common point. For example, [1,2] and [3,4] are non-overlapping, but [1,2] and [2,3] are overlapping.

START=0
END=1

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        start = newInterval[START]
        end = newInterval[END]
        result = []

        i = 0
        while i < len(intervals) and intervals[i][END] < start: 
            result.append(intervals[i])
            i += 1

     
        if len(intervals) > 0 and i < len(intervals) and intervals[i][START] <= start and intervals[i][END] >= end: return intervals

        result.append(newInterval)
        newIndex = len(result) - 1
        
        if len(intervals) > 0 and i < len(intervals) and intervals[i][START] < start: 
            result[newIndex][START] = intervals[i][START]
            i+=1
    

        while i < len(intervals) and start <= intervals[i][START] and end >= intervals[i][END]:
            i += 1

        print(result)
        print(f'i: {i}')

        if i < len(intervals) and intervals[i][START] <= end:
            result[newIndex][END] = intervals[i][END]
            i += 1

        while i < len(intervals):
            result.append(intervals[i])
            i +=1

        return result
        

intervals=[[1,2],[3,5],[9,13]]
newInterval=[4,10]
print (f'intervals {intervals}')
print (f'new {newInterval}')


sol = Solution()
res = sol.insert(intervals, newInterval)
print(res)





