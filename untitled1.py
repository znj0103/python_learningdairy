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
#分支和循环实战
#例1 100以内的素数 第一次没做出来
# print('100内的素数有：',end=' ')
# for num in range(1,101,1):
#     is_prime = True
#     for i in range(2,num,1):
#         if num%i ==0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num,end=',')

#例2 斐波那契数列 改进：a,b = b ,a+b;i变成_
# b = 1
# print('1','1',end=',')
# for i in range(1,21):
#    sum = a+b
#    a = b
#    b = sum
#    print(sum,end=',')

#例3 寻找水仙花数
# for i in range(100,1000):
#     a = i//100
#     b = i//10%10
#     c = i % 10

#     if i == a**3 + b**3 + c**3:
#         print(f'{i}为水仙花数')

# #例3.2 正整数反转
# num = int(input(':'))
# while num != 0:
#     out = num%10
#     print(out,end='')
#     num //= 10

#例4 百钱百鸡问题
#穷举法,更好的：c = 100-a-b
# money = 100
# for a in range(20,-1,-1):
#     for b in range(0,34,1):
#         for c in range(0,100,3):
#             if a*5+b*3+c//3 == 100 and a+b+c ==100:
#                 print(f'公鸡{a}只，母鸡{b}只，小鸡{c}只。')

#例5 CRAPS赌博游戏
# import random
# money = 1000

# win_number = 0
# while money >0:
#     if win_number == 0 :
#         duzhu = int(input(f'现在你还有{money}元，请下注：'))
#         if duzhu == 0:
#              break
#         else:
#             number1 = random.randint(1,7)
#             number2 = random.randint(1,7)
#             print(f'骰子：{number1},{number2}')
#             if number1+number2 in [7,11]:
#                 print(f'玩家首次就获胜,赢了{duzhu}元')
#                 money += duzhu
#             elif number1+number2 in [2,3,12]: 
#                 money -= duzhu
#                 print(f'庄家获胜，现在你还有{money}元钱')
#             else: 
#                 win_number = number1+number2
#                 print(f'平局，现在你还有{money}元钱，获胜数字为{win_number
#                                                     }')
#     else:
#         number1 = random.randint(1,7)
#         number2 = random.randint(1,7)
#         print(f'骰子：{number1},{number2}')
#         if number1+number2 == win_number:
#                 print(f'玩家终于获胜,赢了{duzhu}元')
#                 money += duzhu
#                 win_number = 0
#         elif number1+number2 == 7:
#                 money -= duzhu
#                 print(f'庄家获胜，现在你还有{money}元钱')
#                 win_number = 0
# else:print('玩家破产')

#DAY08 常用数据结构 列表-1
#list 数据类型 容器
# items1 = [35, 12, 99, 68, 55, 35, 87]
# print(type(items1))

# items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
# items8[1:3] = ['x', 'o']
# print(items8)

#例1 重写骰子代码
# import random
# items = [0,0,0,0,0,0]
# for _ in range(6000):
#     number = random.randint(1,6) - 1
#     items[number] +=1
# print(items)
#终于学完了！！！！！！！累死我也（2025，12，9，21:37）
