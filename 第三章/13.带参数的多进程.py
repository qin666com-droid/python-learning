"""
 案例:演示带参数的多进程

 进程传参有两种方式:
    1. 通过args参数传参, 接收所有的 位置参数
    2. 通过kwargs参数传参, 接收所有的 关键字参数

"""
#导包
import multiprocessing,time,os

#需求:小明一边敲代码,一边听音乐
# 1. 定义函数,表示 编写代码
def coding(name,num):
    for i in range(1,num +1):
        time.sleep(0.1)
        print(f"{name}正在敲第{i}遍代码!")
    # print(f"p1进程的pid是:{os.getpid()},{multiprocessing.current_process().pid},父进程ppid是:{os.getppid()}")

# 2. 定义函数,表示 听音乐
def music(name,count):
    for i in range(1,count +1):
        time.sleep(0.1)
        print(f"{name}正在听第{i}首音乐......")
    # print(f"p2进程的pid是:{os.getpid()},{multiprocessing.current_process().pid},父进程ppid是:{os.getppid()}")


# 3. 创建进程对象,分别关联上诉的两个 目标函数
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=coding,args=("扶苏",10))
    p2 = multiprocessing.Process(target=music,kwargs={"count":5,"name":"乔松"})

    # 4. 启动进程
    p1.start()
    p2.start()
