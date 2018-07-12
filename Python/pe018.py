#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 18
# Maximum path sum I

import numpy as np


a = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''.split("\n")
b = [i.split(' ') for i in a]
c = []
for line in b:
    c.append([int(i) for i in line])

linecount = 2
allline = [[75], [95 + 75, 64 + 75]]
for cline in c[2:]:
    tmpline = np.zeros(len(cline))
    tmpline[0] = cline[0] + allline[linecount - 1][0]
    tmpline[-1] = cline[-1] + allline[linecount - 1][-1]
    for k in np.arange(len(cline))[1:-1]:
        tmpline[k] = max(allline[linecount - 1][k - 1], 
                         allline[linecount - 1][k]) + cline[k]
    allline.append(list(tmpline))
    linecount += 1
    
print(max(allline[-1]))    

# 1074
# 0.002 s
