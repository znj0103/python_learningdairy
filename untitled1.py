#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 25 13:24:46 2025

@author: znj
"""
# import sys

# x = int(input('公因数1:'))
# y = int(input('公因数2:'))

# z = 1
# q = 1
# for i in range(x, 1 ,-1):
#     if x%i == 0:
#         z = i
#         for j in range(y, 1 ,-1):
#             if y%j == 0:
#                 q = j
#                 if q == z:
#                     break

# print('公约数为：',q)   

# print("hello world")
# print("b")

#05-分支结构
#if elif结构
#match case结构 ,| 与 _
#分支结构的应用
#例1:分段函数求值

# x  = float(input("请输入x的值:"))
# if x > 1:
#     y = 3*x - 5
# elif -1 <= x <= 1:
#     y = x + 2
# elif x < -1:
#     y = 5*x + 3

# print(f'{y =}')

#例2 百分制转化
# score = float(input("请输入你的成绩："))
# if score >=90:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70<= score < 80:
#     grade = "C"
# else: grade ="D"

# print(f'{grade =}')

#例3 计算三角形的周长和面积
# a = float(input("边1:"))
# b = float(input("边2:"))
# c = float(input("边3:"))
# if a+b >c and a+c > b and b+c > a:
#     perimeter = a+b+c
#     p = perimeter/2
#     area = (p*(p-a)*(p-b)*(p-c))**0.5
#     print(f'周长={perimeter}')
#     print(f'面积={area}')
# else:
#     print("不能构成三角形")