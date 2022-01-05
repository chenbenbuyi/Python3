import re

dic = {}


# 找出指定内容中指定的各名字出现的次数

def statistics(file1, file2):
    f1 = open(file1, encoding='utf-8')
    names = f1.read().split('、')
    f2 = open(file2, 'r', encoding='utf-8')
    content = f2.read().replace('\n', '')
    for name in names:
        name_num = re.findall(name, content)
        dic[name] = len(name_num)


statistics("name.txt", "sanguoyanyi.txt")
print(dic)
