import unittest
import sys

def combo(string):
    return _combo(''.join(sorted(set(string))))

def _combo(string):
    if len(string) == 1:
        return [string]

    combos = []

    for i in range(len(string)):
        combos.append(string[i])
        for result in _combo(string[i+1:]):
            result = string[i] + result
            combos.append(result)

    return combos

class CharactersTestCase(unittest.TestCase):
    def testCharactersA(self):
        input = 'ab'
        result = ['a', 'b', 'ab']
        self.assertCountEqual(combo(input), result)

    def testCharactersB(self):
        input = 'elmn'
        result = [
                'e', 'l', 'm', 'n',
                'el', 'em', 'en', 'lm', 'ln', 'mn',
                'elm', 'eln', 'emn', 'lmn',
                'elmn'
                ]

        self.assertCountEqual(combo(input), result)

if __name__ == '__main__':
    for c in combo(sys.argv[1]):
        print(c)
