class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # Step 1: Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]  # Initialize with the first interval
        
        # Step 2: Iterate through the sorted intervals
        for i in range(1, len(intervals)):
            prev = merged[-1]
            curr = intervals[i]

            if curr[0] <= prev[1]:  # Overlapping intervals
                prev[1] = max(prev[1], curr[1])  # Merge them
            else:
                merged.append(curr)  # Add non-overlapping interval

        return merged


