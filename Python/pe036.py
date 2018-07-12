#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 36
# Double-base palindromes

import numpy as np


allist = []
for i in np.arange(1, 1000001):
    pself = str(i) == str(i)[::-1]
    pbi = bin(i)[2:] == bin(i)[2:][::-1]
    if pself and pbi:
        allist.append(i)
        
print(sum(allist))

# 872187
# 1.909 s
