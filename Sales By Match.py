#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    c = Counter(ar)
    count = 0
    for i in c:
        count += c[i] // 2
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
