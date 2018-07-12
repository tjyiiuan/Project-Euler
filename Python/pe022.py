#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 22
# Names scores

allname = open(r"path\to\p022_names.txt").read().replace('"', '').split(",")
allname.sort()

score = lambda name: sum([ord(k) - 64 for k in name])
    
namescore = 0
for i in range(len(allname)):
    namescore += (i + 1) * score(allname[i])
    
print(namescore)

# 871198282
# 0.0196 s
