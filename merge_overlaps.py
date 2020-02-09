import unittest

class MergeOverlapsTestCase(unittest.TestCase):
    def testMergeOverlapsA(self):
        intervals = [(1,4), (2,5), (6,7)]
        result = [(1,5), (6,7)]
        self.assertListEqual(self.mergeOverlaps(intervals), result)

    def testMergeOverlapsB(self):
        intervals = [(1,5), (3,7), (6,9), (2,3)]
        result = [(1,9)]
        self.assertListEqual(self.mergeOverlaps(intervals), result)

    def testMergeOverlapsC(self):
        intervals = [(1,10), (4,6)]
        result = [(1,10)]
        self.assertListEqual(self.mergeOverlaps(intervals), result)

    def mergeOverlaps(self, intervals):
        intervals.sort(key=lambda x: x[0])
        result = []
        start, end = intervals[0]
        for interval in intervals[1:]:
            next_start, next_end = interval
            if next_start > end:
                result.append((start, end))
                start = next_start
            if next_end > end:
                end = next_end
        result.append((start, end))
        return result
