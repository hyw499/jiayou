#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :a_1.py
# @Time      :2020/11/12 13:57
# @Author    :liz

#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# for x in range(1,5):
#     for y in range(1,5):
#         for z in range(1,5):
#             if x!=y and x!=z and y!=z:
#                 print(f"{x}{y}{z}")

 # 使用 函数  写
# def ZuHe(i,j):
#     for x in range(i,j):
#         for y in range(i,j):
#             for z in range(i,j):
#                 if x != y and x != z and y != z:
#                     print(f"{x}{y}{z}")
# ZuHe(2,5)

'''
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''
# I = int(input(">>>"))
# if I>0:
#     bonus = 100000 * 0.1
#     if I>100000 and I<=200000:
#         bonus += (I-100000) *0.075
#     elif I>200000:
#         bonus+=100000*0.075
#         if I>200000 and I<=400000:
#             bonus+=(I-200000)*0.05
#         elif I>40000:
#             bonus+= 200000 *0.05
#             if I>400000 and I<=600000:
#                 bonus+=(I-400000)*0.03
#             elif I>600000:
#                 bonus +=  200000 * 0.03
#                 if I>600000 and I<=1000000:
#                     bonus+=(I-600000)*0.015
#                 elif I>1000000:
#                     bonus +=  400000 * 0.01
#
# print(bonus)

#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# for i in range(1000):
#     for j in range(1,i):
#         if j**2==i+100:
#             for m in range(i):
#                 if m**2==i+268:
#                     print(i)

#输入某年某月某日，判断这一天是这一年的第几天？
# time = input(">>>")
# year = time[0:4]
# month= time[4:6]
# day = time[6:8]
# list1=[0,0,31,59,90,120,151,181,212,243,273,304,334,365]
# for i in range(len(list1)):
#     if int(month) ==  i:
#         print(list1[i] + int(day))

#  输入三个整数x,y,z，请把这三个数由小到大输出
# x = int(input(">>>"))
# y = int(input(">>>"))
# z = int(input(">>>"))
# if x>y:
#     x,y = y,x
# if y>z:
#     y,z=z,y
# print(x,y,z)

#取任意位数的斐波那契数列
# def aa(x):
#     a = 1
#     b = 1
#     for i in range(x-4):
#         a,b=b,a+b
#     print(a+b)
#
# aa(10)


#    查找按照指定字符开头和结尾的
# list1=['12345','abcsdfg','123wsad45','mkoog','abc45','123dfg',12345]
# for i in list1:
#     if str(i).startswith('123'):
#         if str(i).endswith('45'):
#             print(i)

#        去重并排序
# list1=[123,456,67,10,100,455,687,456,100]
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)
# for m in range(len(list2)):
#     for n in range(len(list2)-1):
#         if list2[m]<list2[n]:
#             list2[m],list2[n]=list2[n],list2[m]
# print(list2)

#判断字符串是否回文

# str1 = input(">>>")
# str2 = str1[::-1]
# if str1 == str2:
#     print("yes")
# else:
#     print("no")

#排序（选择、冒泡）

# list1=[123,456,67,10,100,455,687,456,100]
# for i in range(len(list1)):
#     for j in range(len(list1)-1):
#         if list1[i]>list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
# print(list1)


# for i in range(len(list1)):
#     for j in range(len(list1)-i-1):
#         if list1[j]>list1[j+1]:
#             list1[j],list1[j + 1]=list1[j+1],list1[j]
# print(list1)

#三次猜数字
# import random
# ai = random.randint(1,10)
# num = 3
# while num>0:
#     player = int(input(">>>"))
#     if player<ai:
#         print(f'比{player}大，您还有{num-1}次机会')
#         num=num-1
#         continue
#     elif player>ai:
#         print(f'比{player}小，您还有{num - 1}次机会')
#         num = num - 1
#         continue
#     else:
#         print("您猜对了")
#         break

#水仙花数
# for i in range(100,1000):
#     a = i//100
#     b = i//10%10
#     c = i%100%10
#     if a**3+b**3+c**3==i:
#         print(i)

#十进制转十六进制
# def Jin_Zhi(x,y):
#     list1 = [str(i) for i in range(10)] + [chr(i) for i in range(97, 103)]
#     print(list1)
#     str2 = ' '
#     while True:
#         x , z = divmod(x,y)
#         str2 += list1[z]
#         if x==0:
#             break
#     print(str2)
# Jin_Zhi(16,16)

#  质因数之和等于他本身
# i = int(input(">>>"))
# list1 = []
# for x in range(2,i):
#         if i%x==0:
#             # print(x)
#             for y in range(2,x):
#                 if x%y==0:
#                     break
#             else:
#                 list1.append(x)
#                 print(list1)
#                 i=i/x
# print(int(i))
# list1.append(int(i))
# list1.sort()
# for m in range(len(list1)):
#     print(list1[m])


#  因数和等于它本身
# for i in range(1,1000):
#     list1 = []
#     for j in range(1,i):
#         if i%j==0:
#             list1.append(j)
#     if sum(list1)==i:
#         print(list1)
#         print(i)

#将列表中最大的放在最后一位，最小的放在第一位
# list1=[3,4,67,43,67,12,78,34,23,37,10]
#
# for i in range(len(list1)):
#     for j in range(len(list1)-1):
#         if list1[i]>list1[j]:
#             list1[i],list1[j]=list1[j],list1[i]
# print(list1)


# 一个有顺序的列表，随机加入一个数，加入的数在正确的位置
# list1=[78, 67, 67, 43, 37, 34, 23, 12, 10, 4, 3]
# x = int(input(">>>"))
# for i in range(len(list1)):
#     if list1[i]>x>list1[i+1]:
#         list1.insert(i+1,x)
#     elif x>max(list1):
#         list1.insert(0,x)
#     elif x<min(list1):
#         list1.insert(len(list1),x)
#     elif x == list1[i]:
#         list1.insert(i + 1, x)
#         break

# print(list1)

#用100元买100只鸡，公鸡2元一只，母鸡1元一只，小鸡0.5元一只，问买公鸡、母鸡、小鸡各几只
# for g in range(50):
#     for m in range(101):
#         for x in range(101):
#             if g+m+x==100 and 2*g+m+0.5*x==100:
#                 print(g,m,x)

#一个函数，传两个参数a,b，a是列表，b是一个数字，找出a数组中两数之和等于b，打印出来这两个数
def D_yin(x,y):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]+x[j]==y:
                print(x[i],x[j])

# D_yin([0,1,2,3,4,5,4,6,8,9,12,15,17,11,19,20],20)

#  操作任意一个txt文件，将文件中的小写字母全部替换成大写字母
# file1 = open(r"a.txt","r",encoding="utf-8")
# a = file1.read()
# b = a.upper()
# file2 = open(r"a.txt","w",encoding="utf-8")
# file2.write(b)
# print(b)

#写一个函数，检查传入的字典的每一个值的长度，如果长度大于2，则保留该值的前两位的字符，
# 如果不大于2，则不做任何改变。
# dict1 = {'name':'tom','sex':'man','age':'20','class':'3'}
# for key,values in dict1.items():
#     if len(values)>2:
#         dict1[key]=values[0:2]
#         print(dict1)

#写一个函数，统计传入函数的字符串中有多少是字母、数字、空格、其他的个数，显示统计的结果。
# def IS(x):
#     a =0
#     b =0
#     c =0
#     for i in x:
#         if i.isalpha():
#             a+=1
#         elif i.isdigit():
#             b+=1
#         elif i.isspace():
#             c+=1
#     print(a,b,c)
# IS('1234sa dfg ')


# 打印出某个目录下所有的txt文件
# import os
# file1 = os.listdir()
# print(file1)
# for i in file1:
#     if i.endswith('.txt'):
#         print(i)


#      文件备份
# def beifen(x): # x 为文件名 , 前三行备份文件名
#     hou = x.find('.') #找到文件名中 . 的下标位置
#     new_file=(x[:hou]+'副本'+x[hou:]) # 文件名字中下标从开始到 . 的前一个，加上副本和 包含.和 . 后面的所有

#     file1=open(x,'rb') # 备份内容，以二进制的方法打开文件
#     m = file1.read()     # 读取原文件的所有内容
#     file2=open(new_file,'wb') # 以二进制的方式打开新文件
#     file2.write(m)  把原文件的内容写入备份文件
      file1.close() #关闭文件
      file2.close()
# beifen('a.txt')

#  统计某个目录下有多少目录文件、普通文件
# import os
# file1= os.listdir()
# a=0
# b=0
# for i in file1:
#     if os.path.isfile(i):
#         a+=1
#     elif os.path.isdir(i):
#         b+=1
# print(a,b)

# 从键盘上输入若干个学生的成绩，统计出平均成绩并输出低于平均分的学生成绩，用输入负数结束输入
list1 = []
while True:
    coure = input(">>>")
    if coure < str(0) :
        break
    new_str=coure.split(',')
    for i in new_str:
        list1.append(int(i))
    x=sum(list1)
    y = x/len(list1)
    for j in list1:
        if j < y:
            print(j)
















