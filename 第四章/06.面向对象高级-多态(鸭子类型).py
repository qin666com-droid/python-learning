"""
鸭子类型:
        如果它走路像鸭子,叫起来像鸭子,那它就是鸭子
        --关注的是对象的行为,而不是它的类型
"""



class Duck:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age} 岁的 {self.name} 正在游泳....')

class Dog :
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age} 岁的 {self.name} 正在游泳....')

class Pig:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age} 岁的 {self.name} 正在游泳....')


def go_swimming(duck):
    duck.swimming()

#测试代码
if __name__ == '__main__':
    go_swimming(Dog('旺财',1))
    go_swimming(Duck("逃离鸭",5))
    go_swimming(Pig('八戒',2))
