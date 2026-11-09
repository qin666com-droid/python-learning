"""
案例:演示多进程

多进程的目的:
    它属于多任务的一种实现方式,目的是充分利用CPU资源,提高程序的执行效率

实现方式:
    1. 导入multiprocessing模块
    2. 创建进程对象
    3. 启动进程
    4. 等待进程结束
    5. 关闭进程对象
"""
#导包
import multiprocessing
import time
#1. 定义函数,表示 编写代码
def fun_code():
    for i in range(1,11):
        time.sleep(0.1) #可以模拟耗时操作,更好的查看多任务的执行效果
        print(f"正在敲第{i}遍代码")


#2. 定义函数,表示 听音乐
def fun_music():
    for i in range(1,11):
        time.sleep(0.1)
        print(f"正在听第{i}首音乐......")


#3.创建两个进程对象,分别关联上诉的两个 目标函数
# 细节:通过main进程(主进程)来启动两个子进程
if __name__ == "__main__":
    # 单进程
    # fun_code()
    # fun_music()

    # 进程p1关联 fun_code函数,p1进程抢到CPU资源,执行fun_code函数
    p1 = multiprocessing.Process(target=fun_code)
    p2 = multiprocessing.Process(target=fun_music)

    # 4.启动进程,大白话:表示进程启动了,就可以抢占CPU资源,执行函数体

    p1.start()
    p2.start()

