import unittest
from datetime import datetime, timedelta
from collections import deque

class Throttle:
    def __init__(self, maxreq, secs):
        self.maxreq = maxreq
        self.deltas = deque([0]*maxreq, maxreq)
        self.nreq = 0
        self.lastt = 0
        self.secs = secs

    def throttle(self, reqt):
        if self.nreq < self.maxreq:
            self.deltas.append(reqt - self.lastt)
            self.lastt = reqt
            self.nreq += 1
            return False

        dt = reqt - self.lastt
        self.deltas.append(dt)

        tott = 0
        nreq = 0

        for delta in reversed(self.deltas):
            tott += delta
            nreq += 1

            if tott >= self.secs:
                break

        if nreq < self.maxreq:
            # requests far enough apart
            self.lastt = reqt
            self.nreq += 1
            return False
        else:
            # exceeded maxreq inside time limit
            return True

class Throttle10PerSecTestCase(unittest.TestCase):
    def test20RequestsPerSecond(self):
        throttle = Throttle(10, 1000)
        throttled = False
        tt = 0
        nreq = 0

        for i in range(20):
            throttled = throttle.throttle(tt)
            tt += (1000/20)
            if throttled:
                break
            nreq += 1

        self.assertTrue(throttled)
        self.assertEqual(nreq, 10)

    def testTwoRequestsPerSecond(self):
        throttle = Throttle(10, 1000)
        throttled = False
        tt = 0
        nreq = 0

        for i in range(20):
            throttled = throttle.throttle(tt)
            tt += 500
            if throttled:
                break
            nreq += 1

        self.assertFalse(throttled)
        self.assertEqual(nreq, 20)

