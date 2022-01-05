# python 基础规则介绍

import time
# 使用 import 导入需要的组件模块

# 通过缩进而不是用 {} 来控制类、函数；也并不需要以 : 作为语句的结束符号，而是以新行作为上一行的结束符
if 1 > 0:
    print('缩进测试')
else:
    print('缩进测试')

'''
 常见数据类型使用介绍 
  整型   100
  浮点数  100.4
  字符串  '字符串'
  布尔值  False True
  类型之间的转换也很方便如
  int('123') 将字符串转为 int
  str(123) 将 整型数字转为 字符串
'''
print(type(123))  # 数据类型获取

'''
变量的定义和使用
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
'''
p = 100
b = p
print(b / 5)

'''
 序列
 序列程序都是有序排列，可以通过下标偏移量访问其单个或多个成员
 字符串、列表、元祖(元组（tuple）与列表类似，不同之处在于元组的元素不能修改)都属于序列
 “字符串”
 ['列表元素',123,False]
 ("abc","ef")
 序列的几种基本操作方式：
    成员关系操作符   对象[not]in 序列
    连接操作     序列+序列
    重复操作     序列*3
    切片操作     序列[0:整数]
 
'''
tiangan = '甲乙丙丁戊己庚辛壬癸'
print(tiangan[3])
print(tiangan[0:4])  # 左闭右开，从偏移量为0的元素开始到偏移量为4的元素，但不包含4
print('甲乙' not in tiangan)
print(tiangan * 3)

# 元组测试
yuanzu = ("甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸")
yz = ()  # 空元组
yz2 = ("sd",)  # 声明只有一个元素的元组
(a, b) = ("甲", "乙")
# 列表测试
a_list = ["a", "b"]
a_list.append("d")
print(a_list)

"""
条件与循环
for 循环 
    for x in 序列
while 循环
    while True:
        todo

"""
# a = input('请输入条件判断值：')
a = 'abc'

if a == 'abc':
    print("条件成立")
elif a == 'ed':
    print("elseif 判断")
else:
    print("输入的值 %s 不匹配" % a)
# for 循环
for i in a:
    print(i)

# while 循环
num = 5
while True:
    if num == 7:
        num += 3
        continue  # 跳过档次循环
    print(num)
    num += 1
    if num == 110:
        break  # 循环停止

'''
字典（映射类型，类似于Java中的 Map）
'''
dic_man = {'name': '陈小远', 'age': 18}
dic_man['addr'] = "这是我的住址"
print(dic_man)

'''
 列表推导式和字典推导式
'''
# 实现从 1到10 所有偶数的平方
b_list = []

for i in range(1, 11):  # 使用常规方式实现
    if (i % 2 == 0):
        b_list.append(i * i)

b_list = [i * i for i in range(1, 11) if (i % 2 == 0)]  # 使用列表推导式的方式
b_dic = {i: 0 for i in dic_man}  # 字典推导式
print(b_list)
print(b_dic)
