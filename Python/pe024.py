#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 24
# Lexicographic permutations

from itertools import permutations

import numpy as np


a = [int(''.join(k)) for k in 
     list(permutations([str(i) for i in np.arange(10)], 10))]
a.sort()
print(a[999999])

# 2783915460
# 3.190 s
