#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 23
# Non-abundant sums

import numpy as np
limit = 28124

def finddivsor(num):
    div = []
    for i in np.arange(1, int(num/2)+1):
        if not num % i:
            div.append(i)
    return div

allabnum = []
for i in np.arange(limit ):
    if sum(finddivsor(i)) > i:
        allabnum.append(i)

def issum(num):
    for i in allabnum:
        if i > num/2 + 1:
            return False
        
        if (num - i) in allabnum:
            return True
        
    return False
    
absumlist = np.ones(limit + 1)
for k in np.arange(len(allabnum)):
    for j in np.arange(k, len(allabnum)):
        sumnum = allabnum[k] + allabnum[j]
        if sumnum > limit:
            break 
        absumlist[sumnum] = 0
        
print(sum(np.where(absumlist)[0]))

# 4179871
# 39.117 s
