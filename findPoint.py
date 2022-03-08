#!/bin/python3

import os
import sys

#
# Complete the findPoint function below.
#
def findPoint(px, py, qx, qy):
    print(2*qx-px,2*qy-py)


n = int(input())

for n_itr in range(n):
    pxPyQxQy = input().split()

    px = int(pxPyQxQy[0])

    py = int(pxPyQxQy[1])

    qx = int(pxPyQxQy[2])

    qy = int(pxPyQxQy[3])

    findPoint(px, py, qx, qy)
