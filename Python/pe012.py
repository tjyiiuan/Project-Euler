#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 12
# Highly divisible triangular number

from itertools import groupby

def getp(num):
    factors = []
    tmp = 2

    while num >= tmp:
        k = num % tmp
        if not k:
            factors.append(tmp)
            num /= tmp
        else:
            tmp += 1 
    factors.sort()
    
    i = 1
    for j,k in groupby(factors):
        i *= len(list(k)) + 1
    return i

count = 10000
while True:
    num = count * (count + 1) / 2
    if getp(num) >= 500:
        print(int(num))
        break
    count += 1
    
# 76576500
# 1.451 s
