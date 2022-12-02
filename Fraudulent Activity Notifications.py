#!/bin/python3

import math
import os
import random
import re
import sys

f = [0] * 201
def oddmedian(d):
    s = 0
    for i in range(201):
        s = s + f[i]
        if s >= d // 2:
            return i

def evenmedian(d):
    s = 0
    a, b = 0, 0
    for i in range(201):
        s = s + f[i]
        if s == d // 2:
            a = i
        elif s > d // 2:
            b == i
    return (a + b) / 2

def activityNotifications(expenditure, d):
    window = expenditure[:d]
    count = 0
    for i in window:
        f[i] += 1
    if d & 1 == 1:
        for i in range(d, len(expenditure)):
            print(f)
            m = oddmedian(d)
            print(m)
            if expenditure[i] >= 2 * m:
                count += 1
            f[expenditure[i-d]] -= 1
            f[expenditure[i]] += 1
    else:
        for i in range(d, len(expenditure)):
            print(f)
            m = evenmedian(d)
            print(m)
            if expenditure[i] >= 2 * m:
                count += 1
            f[expenditure[i-d]] -= 1
            f[expenditure[i]] += 1  
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
