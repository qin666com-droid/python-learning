"""
案例: 线程入门案例,一边听音乐,一边写代码

线程的使用步骤:
    1. 导入线程模块
    2. 创建线程对象
    3. 启动线程


线程与进程的关系:
    1.进程是CPU分配资源的基本单位,线程是CPU调度资源的最小单位
    2.线程是依附于进程的,每个进程至少有1个线程(主线程栈)
    3.进程间数据相互隔离,(同一个进程的)线程间数据可以共享
"""
import multiprocessing
#1.导入线程模块
import threading

def coding():
    for i in range(1,10):
        print(f"正在写第{i}行代码")

def music():
    for i in range(1,10):
        print(f"正在听第{i}首音乐")

if __name__ == '__main__':
    #1.创建线程对象
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=music)
    #2.启动线程
    t1.start()
    t2.start()
