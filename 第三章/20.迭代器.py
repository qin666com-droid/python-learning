"""
案例: 演示自定义迭代器

迭代器介绍:
    概述:
        自定义的累,只要重写了_iter_()和 _next_()方法,就可以称为 迭代器
    目的:
        隐藏底层的逻辑,让用户使用更方便
        惰性加载,用的时候才会获取

"""
#需求:模拟range(1,6),自定义 迭代器实现同等逻辑
 #场景1:回顾range()用法
for i in range(1,6):
    print(i)
print("*"*20)

#场景2: 自定义迭代器
#1.自定义 迭代器类
class MyIterator:
    #2.通过init魔法方法,初始化属性,指定: 范围
    def __init__(self,start,end):
        self.current_value = start #当前值等于开始值
        self.end = end             #结束值

    #3. 重写iterator魔法方法,返回当前对象(即: 迭代器对象)
    def __iter__(self):
        return self

    #4.重写next魔法方法,返回当前值,并更新当前值
    def __next__(self):
        #4.1 判断当前值范围是否合法
        if self.current_value >= self.end:
            raise StopIteration                # 抛出异常,迭代结束
        #4.2 走这里,说明当前值合法,返回当前值,并更新当前值
        # value = self.current_value                    #1,2,3,4,5,6
        # self.current_value = self.current_value + 1   #2,3,4,5,6,7
        # return value

        #化简
        self.current_value +=  1
        return self.current_value-1

#创建迭代器对象,并遍历
for i in MyIterator(1,6):
    print(i)
