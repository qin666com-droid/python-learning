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

    def charge(self):
        print(f'{self.brand} {self.model} 正在补充燃油.....')




#燃油车
class FuelCar(Car):
    def charge(self):
        #方式一:super().方法名()
        # super().charge()

        #方式二:类名.方法名(self)
        Car.charge(self)


        print(f'{self.brand} {self.model} 正在加油.....')


#电车
class ElectricCar(Car):
    def charge(self):
        # 方式一:super().方法名()
        # super().charge()

        # 方式二:类名.方法名(self)
        Car.charge(self)

        print(f'{self.brand} {self.model} 正在充电.....')


if __name__ == '__main__':
    c1 = FuelCar('奔驰','奔驰S级','白色','扶苏')
    c1.charge()
    c2 = ElectricCar('奔驰','奔驰E级','黑色','乔松')
    c2.charge()
 