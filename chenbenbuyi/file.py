# 测试 Python 对文件的操作
"""
 文件操作常用的内建函数：
 open   打开文件
 read   读取文件所有 内容
 readline  读取一行
 readlines  读取多行
 seek   文件移动
 write   向文件写入内容
 close   关闭文件
"""

# file = open('test.txt', 'w')
# file.write('写入文件的内容\r')
# file.close()
#
# file2 = open('test.txt', 'a')
# file2.write('给文件追加新的内容')
# file2.close()

# file2 = open('test.txt')
# print(file2.read())
# file2.close()

# file2 = open('test.txt')
# for i in file2.readlines():
#     print(i)
# file2.close()

'''
遇见异常：io.UnsupportedOperation: can't do nonzero end-relative seeks
Pyhon3在文本文件中，没有使用b模式选项打开的文件，只允许从文件头开始计算相对位置，从文件尾计算时就会引发异常
在开始使用open打开文件时候，将打开方式从r，换成rb即可
'''

file2 = open('test.txt',"rb")
print("当前文件位置：%s" % file2.tell())
file2.read(1)
print("当前文件位置2：%s" % file2.tell())
# 第一个参数表示偏移位置，第二个参数有三个值， 0  表示从文件开始偏移，1 表示从当前位置偏移， 2 从文件结尾偏移
file2.seek(1,2)
print("当前文件位置3：%s" % file2.tell())
file2.close()