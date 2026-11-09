"""
案例:演示单任务,前边不执行完毕,后边绝对不能执行
"""

#1.定义函数A,输出10次 "hello world"
def fun_a():
    for i in range(10):
        print("hello world")

#2.定义函数B,输出10次 "hello python"
def fun_b():
    for i in range(10):
        print("hello python")
fun_a()
print("*"*20)
fun_b()
