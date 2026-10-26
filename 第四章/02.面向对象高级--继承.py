"""
继承:描述的是两类之间的关系,子类继承父类的属性和方法(非私有),
    并可以添加自己的属性和方法

"""
class Car:
    def __init__(self,brand,model,color,owner):
        self.brand = brand          #型号   公有属性
        self.model = model          #型号  公有属性
        self.color = color          #颜色  公有属性

        self.__owner = owner        #车主  �私有属性

    def start(self): #启动汽车
        print(f'{self.brand} {self.model} 正在启动.....')

    def run(self): #汽车运行
        print(f'{self.__owner} :{self.brand} {self.model} 正在运行.....')
        self.__control_fuel()
    def stop(self): #汽车停止
        print(f'{self.brand} {self.model} 正在停止.....')

    def __control_fuel(self):
        print(f'{self.brand} {self.model} 正在控制燃油.....')

    def get__owner(self):
        return self.__owner[0:1] +"**"











#燃油车
class FuelCar(Car):
    pass



#电车
class ElectricCar(Car):
    pass


if __name__ == '__main__':
    c1 = FuelCar('奔驰','奔驰S级','白色','扶苏')
    c1.run()
    c1.stop()
    c1.start()
    print(c1.brand)
    print(c1.model)
    print(c1.color)
    print(c1.get__owner())

