#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 14:33:31 2018

@author: adityamishra
"""

import sys

import numpy as np


def optimal_weight(W, w):
    # write your code here

    matrix = np.zeros(shape=(len(w), W + 1), dtype=int)

    for j in range(0, len(w)):
        for i in range(1, W + 1):
            if w[j] > i:
                matrix[j, i] = matrix[j - 1, i]
            else:
                matrix[j, i] = max(w[j] + matrix[j - 1, i - w[j]], matrix[j - 1, i])
    return matrix[len(w) - 1, W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))