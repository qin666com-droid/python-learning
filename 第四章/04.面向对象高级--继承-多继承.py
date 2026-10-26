"""
多继承:一个子类可以继承多个父类,每个父类可以有多个子类,
形成一个树状结构,每个节点都是一个类,每个分支都是一个继承关系

"""


class Car:
    def __init__(self, brand, model, color, owner):
        self.brand = brand  # 型号   公有属性
        self.model = model  # 型号  公有属性
        self.color = color  # 颜色  公有属性

        self.__owner = owner  # 车主  �私有属性

    def start(self):  # 启动汽车
        print(f'{self.brand} {self.model} 正在启动.....')

    def run(self):  # 汽车运行
        print(f'{self.__owner} :{self.brand} {self.model} 正在运行.....')

    def stop(self):  # 汽车停止
        print(f'{self.brand} {self.model} 正在停止.....')


    def get__owner(self):
        return self.__owner[0:1] + "**"

    def charge(self):
        print(f'{self.brand} {self.model} 正在补充燃油.....')


#华为智驾
class HuweiAiDrive:
    #华为AI智能驾驶
    def __init__(self,version="V1.0"):
        self.version = version
    def run(self):
        print(f'华为AI智能驾驶{self.version}正在运行.....')


#问界汽车
class WenJieCar(Car,HuweiAiDrive):
    def __init__(self,brand,model,color,owner,version="V1.0"):
        # super().__init__(brand,model,color,owner)
        HuweiAiDrive.__init__(self,version)
        Car.__init__(self,brand,model,color,owner)

    def run(self):
        Car.run(self)
        HuweiAiDrive.run(self)


#MRO:方法解析顺序,根据MRO,先解析左父类,再解析右父类,最后解析子类
if __name__ == '__main__':
    c = WenJieCar('奔驰','奔驰S级','白色','扶苏')
    print(c.__dict__)


    # print(WenJieCar.__mro__)
    # print(WenJieCar.mro())

    c.run()
