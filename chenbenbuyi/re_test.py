'''
 正则表达式 元字符
. 匹配任意单个字符
^ 以什么做开头
$ 以什么结尾
* 前面字符出现 0 次或多次
+ 前面字符出现 1 次或多次
? 前面字符出现 0 次或1 次
{m} {m,n} 表示前面的字符出现括号内的次数或次数范围
[abc] 匹配括号内包含的某个字符
\d 匹配一串数字
\D 匹配不包含数字
\s 匹配只包含 a-z 的字符串
() 分组
^$ 匹配空行
.{3} 任意字符出现3次


'''

import re

p = re.compile('s+')
print(p.match('s'))

#  表示b出现 5次或
p = re.compile('sb{5,7}ds')
print(p.match('sbbbbbbbds'))

# 匹配 包含在中括号中的某个字符
p = re.compile('c[bfs]t')
print(p.match('cbt'))

# 匹配 包含在中括号中的某个字符
p = re.compile('\s')
print(p.match('cbt'))

# 年月日匹配和分组
p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.match('2022-1-22'))
print(p.match('2022-1-22').group())
print(p.match('2022-1-22').group(1))
print(p.match('2022-1-22').group(3))
print(p.match('2022-1-22').groups())

y, m, d = p.match('2020-10-23').groups()
print(m)

# search 进行搜索匹配
p = re.compile(r'(\d+)-(\d+)-(\d+)')
print(p.search('as2022-1-22dss').group())

# sub 替换函数的使用

phone = '12-300-234 # 我要替换注释后的中文'
print(re.sub(r'#.*$', '', phone))
print(re.sub(r'\D', '', re.sub(r'#.*$', '', phone)))
# 在字符前输入 r 原样输出
print(r'\n')
