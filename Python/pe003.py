#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Problem 3
# Largest prime factor

num = 600851475143
i = 2

while i ** 2 <= num:
  if num % i:
    i += 1
  else:
    num //= i
print(num)

# 6857
# 0.001000 s
