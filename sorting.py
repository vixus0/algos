import unittest
import random

def mergeSort(input):
    assert(len(input) > 0)

    if len(input) == 1:
        return input
    elif len(input) == 2:
        if input[0] < input[1]:
            return input
        else:
            return [input[1], input[0]]

    mid = len(input) // 2
    sortedL = mergeSort(input[:mid])
    sortedR = mergeSort(input[mid:])
    sorted = []

    # treat sorted sublists as stacks
    # OR have one index per sublist that gets advanced on 'pop'
    while True:
        if sortedL[0] <= sortedR[0]:
            sorted.append(sortedL.pop(0))
        else:
            sorted.append(sortedR.pop(0))

        if len(sortedL) == 0:
            sorted.extend(sortedR)
            break
        elif len(sortedR) == 0:
            sorted.extend(sortedL)
            break

    return sorted

def quickSort(input):
    def qsort(input, start, end):
        if end - start < 1:
            return
        else:
            pivot = partition(input, start, end)
            qsort(input, start, pivot-1)
            qsort(input, pivot+1, end)

    def prn(pre, input, i, j):
        ijpos = [' ']*len(input)
        ijpos[i] = 'i'
        ijpos[j] = 'j'
        print()
        print(pre + ' ' + ' '.join([str(x) for x in input]))
        print(pre + ' ' + ' '.join(ijpos))

    def partition(input, start, end):
        i, j = start, end - 1

        while True:
            prn('loop', input, i, j)

            while input[i] <= input[end] and i < j:
                i += 1
                prn('i++ ', input, i, j)

            while input[j] >= input[end] and i < j:
                j -= 1
                prn('j-- ', input, i, j)

            if i == j:
                if input[i] <= input[end]:
                    i += 1

                input[i], input[end] = input[end], input[i]
                prn('stop', input, i, j)
                return i
            else:
                input[i], input[j] = input[j], input[i]
                prn('swap', input, i, j)

    qsort(input, 0, len(input)-1)
    return input

class SortingTestCase(unittest.TestCase):
    def testMergeSort(self):
        self.sort(mergeSort)
    def testQuickSort(self):
        self.sort(quickSort)
    def sort(self, sortfn):
        input = random.sample(range(10), 10)
        result = sorted(input)
        self.assertListEqual(sortfn(input), result)
