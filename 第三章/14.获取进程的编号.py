"""
案例:获取进程的编号

进程的编号解释:
     概述:
        在设备中,每个程序(进程)都有一个唯一的编号,称为进程的编号,当程序释放的时候,进程的编号也会被释放
        即:进程id是可以重复使用的
    目的:
        1.查看子进程和父进程的关系,方便 管理
        2.例如: 杀死指定进程,创建子进程....
    格式:
        查看当前进程的pid:
            os模块(operating, 操作系统模块) 的 getpid() 方法()   get Process ID
            multiprocessing模块 的 current_process() 方法()   get Current Process

        查看当前进程的ppid:        parent process id(父进程id)
        os.getppid()
细节:
    main中创建的进程,如果没有特殊指定,它的父进程都是main进程,
    而main进程的父进程是PyCharm程序的pid

"""
#导包
import multiprocessing,time,os

#需求:小明一边敲代码,一边听音乐
# 1. 定义函数,表示 编写代码
def coding(name,num):
    for i in range(1,num +1):
        time.sleep(0.1)
        print(f"{name}正在敲第{i}遍代码!")
    print(f"p1进程的pid是:{os.getpid()},{multiprocessing.current_process().pid},父进程ppid是:{os.getppid()}")

# 2. 定义函数,表示 听音乐
def music(name,count):
    for i in range(1,count +1):
        time.sleep(0.1)
        print(f"{name}正在听第{i}首音乐......")
    print(f"p2进程的pid是:{os.getpid()},{multiprocessing.current_process().pid},父进程ppid是:{os.getppid()}")


# 3. 创建进程对象,分别关联上诉的两个 目标函数
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=coding,args=("扶苏",10))
    p2 = multiprocessing.Process(target=music,kwargs={"count":5,"name":"乔松"})

    # 4. 启动进程
    p1.start()
    p2.start()
    #查看主进程的信息
    print(f"main的pid是:{os.getpid()},{multiprocessing.current_process().pid},父进程ppid是:{os.getppid()}")
