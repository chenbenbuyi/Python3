user1 = {"name": "少鲜", "age": 123}

# 格式化填入参数
print('name is %s ,age is %s ' % (user1["name"], user1['age']))

'''
 类定义
 类名一般大写
 
'''


class Clz1():
    # __init__ 特殊方法，类实例化的时候执行
    # self 表示类本身，类似Java中的this 关键字
    def __init__(self, name, age):
        # 下划线的表示私有字段，不能通过对象.字段 的方式直接访问，子类也无法访问该类型字段
        self.__name = name
        self.age = age

    # 普通方法定义 类中的方法第一个参数一定要用 self
    def print_test(self):
        print("name is %s ,age is %s " % (self.__name, self.age))

    def updateName(self, newname, newage):
        self.__name = newname
        self.age = newage


# 类的实例化
user2 = Clz1("陈小远", 300)
user2.print_test()
user2.age = 235
user2.print_test()
user2.updateName("陈大仙", 234)
user2.print_test()


# 类的继承
class Monster():
    # hp=100 声明变量的时候赋初始值
    def __init__(self, hp=100):
        self.hp = hp

    def run(self):
        print('怪物会跑了：%s' % (self.hp))


class Child(Monster):
    def __init__(self, hp=200):
        # 子类调用父类的方法
        super().__init__(hp)

    def run(self):
        super().run()
        print("子类重写了父类的方法")


a1 = Monster(20)
a1.run()

a2 = Child()
a2.run()
