

"""
435. Non-overlapping Intervals

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:
1 <= intervals.length <= 2 * 104
intervals[i].length == 2
-2 * 104 <= starti < endi <= 2 * 104



"""

class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals: return 0
        intervals.sort( key = lambda s : s[1])
        print(intervals)
        i, j = 0, 1
        count = 0
        while j < len(intervals):
            if intervals[i][1] > intervals[j][0]:  # overlaping between the end[i] and start[i+1]
                print(intervals[i], intervals[j])
                count += 1
                j += 1
            else:
                i = j
                j += 1
        return count





#intervals = [[1,2],[2,3],[3,4],[1,3]]
#intervals = [[1,2],[1,2],[1,2]]
#intervals = [[1,2],[2,3]]
#intervals = [[1,100],[11,22],[1,11],[2,12]]  # Expected:2
#intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]] # Expected:2
intervals = [[1,2],[2,3],[3,4],[-100,-2],[5,7]] # Expected:0

Sol = Solution()
print(Sol.eraseOverlapIntervals(intervals))
