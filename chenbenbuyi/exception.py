0  # Python 异常处理

# 下列示例中，finally 块中是能读取到 try 中声明的变量的，除非 try中变量声明失败，比如文件不存在

try:
    print(1 / 0)
except ZeroDivisionError:
    print("除数不能为0")

try:
    print(1 / 0)
except ZeroDivisionError as  e:
    print("除数不能为 0,%s" % e)

'''
Exception 捕获所有错误
'''
try:
    f = open('test.txt')
except Exception as e:
    print(e)
finally:
    f.close()

try:
    raise NameError('手动抛出错误')
except Exception as e:
    print('自定义错误，错误信息：%s' % e)
