class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        last_end = intervals[0][1]
        remove = 0
        
        for i in range(1, len(intervals)):
            # found overlap
            if intervals[i][0] < last_end:
                remove += 1
                # remove the interval with the longer end
                last_end = min(intervals[i][1], last_end)
            else:
                last_end = intervals[i][1]
            
        return remove