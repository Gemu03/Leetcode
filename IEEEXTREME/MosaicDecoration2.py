import time
from math import ceil
import timeit



class Solution:
    def mosaic(self, w, h, a, b, m, c):
        xCut = yCut = 0
        xCut = h*c if (w % a != 0) else 0
        yCut = w*c if (h % b != 0) else 0
        totalCost = ceil((ceil(w/a) * ceil(h/b))/10) * m  + xCut + yCut
        print(totalCost)

s = Solution()
executionTime = timeit.timeit (lambda: s.mosaic(98765, 43210, 1, 1, 777, 1), number=1)
print("Execution time in ms: ", executionTime * 1000)