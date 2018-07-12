#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 2
# Even Fibonacci numbers

m, n = 1, 2
ssum = 0
while n < 4000000:
    if n % 2 == 0:
        ssum += n
    m, n = n, m + n
print(str(ssum))

# 4613732
# 0.001 s
