#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 4
# Largest palindrome product

x = [x*y for x in range(100,1000) for y in range(100,1000) \
     if str(x*y) == str(x*y)[::-1]]
print(max(x))

# 906609
# 0.568 s
