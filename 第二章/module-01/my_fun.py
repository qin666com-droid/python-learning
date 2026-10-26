#__all__ 指定 from ... import * 导入的是哪些功能
__all__ = ['log1', 'log2', 'PI', 'log4']

#常量(不会发生变化的数据; 常量的名称为全部大写)
PI = 3.14159
NAME = "扶苏"

 #函数
def log1():
     print("- " *30)

def log2():
    print("* " *30)

def log3():
    print("# " *30)

def log4():
    print("$ " *30)

#测试函数
# __name__  :python 中内置变量,表示当前模块的名字(直接运行当前模块,__name__
# 的值为"__main__";当前模块被导入时,__name__的值就是模块的名称)

#执行当前文件,则会执行如下代码;如果当前模块导入,如下代码不执行
if __name__ == '__main__':
    log1()


