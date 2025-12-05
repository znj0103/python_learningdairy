#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 13:24:46 2025

@author: znj
"""
import sys

x = int(input('公因数1:'))
y = int(input('公因数2:'))

z = 1
q = 1
for i in range(x, 1 ,-1):
    if x%i == 0:
        z = i
        for j in range(y, 1 ,-1):
            if y%j == 0:
                q = j
                if q == z:
                    return (q)

print('公约数为：',q)   

print("hello world")
print("test again")


