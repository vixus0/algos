import unittest
from collections import defaultdict

class SortAverageTestCase(unittest.TestCase):
    def testSortAverage(self):
        input = [
                (1000, 4),
                (1000, 7),
                (2000, 10),
                (2000, 8)
                ]
        result = [1000, 2000]
        self.assertListEqual(self.sortAverage(input), result)

    def sortAverage(self, input):
        totals = defaultdict(lambda: 0)
        counts = defaultdict(lambda: 0)

        for point in input:
            id, score = point
            totals[id] += score
            counts[id] += 1

        min = 0
        averages = []

        for id in totals.keys():
            avg = totals[id] / counts[id]

            if avg <= min:
                averages.insert(0, id)
                min = avg
            else:
                averages.append(id)

        return averages
