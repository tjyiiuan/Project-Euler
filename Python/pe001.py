#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 1
# Multiples of 3 and 5

print(sum(i for i in range(1000) if not (i%3 and i%5)))

# 233168
# 0.001 s
