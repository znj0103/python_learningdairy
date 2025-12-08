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


#DAY06 循环结构
# for-in循环
#例1 1-100整数求和
#例2 偶数求和 更改（1，101，2）
# result = 0
# for i in range(1,101,1):
#     result += i

# print(f'结果是{result}')

# #例2.2 利用sum进行求和
# print(sum(range(1,101,2)))
#while循环
#例1.2 利用while循环求和
# i = 1
# result = 0
# while i <=100:
#     result += i 
#     i += 1
# print(f'结果是{result}')
#break continue
#例2.3 利用continue
# total = 0
# for i in range(1,101):
#     if i%2 != 0:
#         continue
#     total += i
# print(f'结果是{total}')

#例3 打印乘法口诀表
# for j in range(1,10):
#     for i in range(1,j+1):
#         if i <= j:
#             # print(i)
#             # print(j)
#             print(f'{i}*{j}={i*j}',end=' ')
#     print('\t')

#例4 判断素数
#增进：判断素数只要？（未完成）
# number = int(input('请输入大于1的整数：'))
# p=000
# if number %1 ==0 and number >=1:
#     for i in range (2,number,1):
        
#         if number %i == 0:
#             print(f'{i}')
#             p = 111
#             break
#         else:p = 222
#     print(f'{number%i,p}')


# match p:
#     case 111:print('不是素数')
#     case 222:print('是素数')
#     case _:print('请输入正确的数字')

#例5 最大公约数
# import sys

# a = int(input('输入第一个数：'))
# b = int(input('输入第二个数：'))
# for i in range(a,0,-1):
#     if a%i ==0:
#         print(f'a:{i}')
#         if b%i == 0:
#             print(i)
#             sys.exit()
#更好的解,更好的：欧几里得算法
# x = int(input('输入第一个数：'))
# y = int(input('输入第二个数：'))
# for i in range(x,0,-1):
#     if x%i == 0 and y%i == 0:
#         print(i)
#         break

#DAY07
