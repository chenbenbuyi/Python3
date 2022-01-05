# import this 可以打印出 python 之禅
import this


# python 中函数的定义
def funa(a, b, c):
    print('a=%s' % a)
    print('b=%s' % b)
    print('c=%s' % c)


# 变长参数的定义
def funb(a, *b):
    print('a=%s' % a)


funb('12')

var1 = 123


def func():
    global var1  # 全局变量定义
    var1 = 456
    print(var1)


func()
print(var1)


#  关键字参数
def fund(param1, start=' '):
    print(start)


fund('必须输入的参数', start='关键字参数传入')

# 迭代器
list1 = [1, 2]
it = iter(list1)
print(next(it))
print(next(it))


# print(next(it))


# 生成器的使用
def frange(start, stop, step):
    x = start
    while x < stop:
        yield x  # yield 生成器，也是迭代器的一种
        x += step


for i in frange(1, 2, 0.5):
    print(i)

# lambda  表达式  python 中使用 lambda 来创建匿名函数。
#
# def fund(x, y):
#     return x + y


fund = lambda x, y: x + y
print(fund(1, 2))
print(fund(1, 2))
