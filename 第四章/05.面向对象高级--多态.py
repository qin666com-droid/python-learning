"""
多态 :是相同一个方法,具有不同的形态,行为,表现


"""

class Car:
    def __init__(self,brand,model,color,owner):
        self.brand = brand  #品牌(公有属性)
        self.model = model  #型号(公有属性)
        self.color = color  #颜色(公有属性)
        self.__owner = owner  #车主(私有属性)


    def start(self):  # 启动汽车
        print(f'{self.brand} {self.model} 正在启动.....')

    def run(self):  #行驶
        print(f'{self.__owner} :{self.brand} {self.model} 正在运行.....')

    def stop(self):  #停止
        print(f'{self.brand} {self.model} 正在停止.....')

    def get_owner(self):
        return self.__owner[0:1] + "**"

    def charge(self):
        print(f'{self.brand} {self.model} 正在补充燃油.....')


# 燃油车
class FuelCar(Car):
    def charge(self):
        print(f'{self.brand} {self.model} 正在补充燃油.....')


#电车
class ElectricCar(Car):
    def charge(self):
        print(f'{self.brand} {self.model} 正在充电.....')



# 补充燃料函数
def handle_charge(car: Car):  #函数参数类声明 --- 指定的是父类型
    car.charge()


#测试代码
if __name__ == '__main__':
    handle_charge(FuelCar("BMW","X5","白色","扶苏"))
    handle_charge(ElectricCar("BYD","汉","白色","zz"))
