#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 5
# Smallest multiple

from math import gcd
from functools import reduce


def lcm(a,b):
    return a*b//gcd(a,b)

print(reduce(lcm,range(1,20+1)))

# 232792560
# 0.001000 s
