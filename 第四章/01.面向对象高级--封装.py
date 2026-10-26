"""
封装: 将数据(属性)和操作数据的方法绑定在一起,形成一个独立的单元(类),
    保护数据不被外部直接访问,通过访问修饰符实现封装
    1.私有属性: 以__开头(在属性名前添加__),在类的外部不能直接访问
    2.私有方法: 以__开头(在方法名前添加__),在类的外部不能直接访问

注意事项:python中没有真正的私有机制;

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



if __name__ == '__main__':
    car = Car('奔驰','奔驰S级','红色','扶苏')
    print(car.brand)
    print(car.model)
    print(car.color)
    # print(car.__owner)
    print(car.get__owner())


    car.start()
    car.run()
    car.stop()
    # car.__control_fuel()
