"""
案例:演示数据的特点

进程的特点:
    1. 进程之间数据是相互隔离的
        因为紫禁城相当于是父进程的"副本",会将父进程的"main外资源"拷贝一份,即: 各是各的
    2.默认情况下,主进程会等待子进程执行结束再结束
        如果要设置主进程结束,子进程同步结束,方式如下:
            思路1:设置子进程为 守护进程
            思路2:强制关闭子进程   可能会导致子进程变成僵尸进程,交由Python 解释器自动回收
                                (底层有 init初始化进程来管理维护)


"""
import multiprocessing,time

# #进程间数据是相互隔离的
# #需求:1.定义1个公共的容器 my_list = [],
#         # 一个进程往里面写数据,另一个进程往里面读数据,看是否能正常读取
# #1.创建1个公共的容器 my_list = []
# my_list = []
#
# #2.定义函数,往容器 my_list 写数据
# def write_data():
#     for i in range(1,10):
#         my_list.append(i)
#         print(f"写数据:{i}")
#     print(f'write_data:{my_list}')
#
# #3.定义函数,从容器 my_list 读数据
# def read_data():
#     time.sleep(0.1)
#     print(f'read_data:{my_list}')
#
#
# #4.创建两个子进程,分别关联上述函数
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=write_data)
#     p2 = multiprocessing.Process(target=read_data)
#
# #5.启动子进程
#     p1.start()
#     p2.start()
#     # print("我是main内资源,看我执行了几次")





#主进程会等待子进程执行结束后再结束,默认情况下
#1.定义函数,表示: 子进程的目标函数
def work():
    for i in range(1,10):
        print("正在努力工作!")
        time.sleep(0.2)

#2.测试
if __name__ == '__main__':
    # 细节:进程的默认命名规则是: Process-编号,编号从1开始
    p1 = multiprocessing.Process(target=work)
    # print(f"p1进程的名字是:{p1.name}")
    #思路1: 设置子进程为 守护进程
    p1.daemon = True #设置p1为: 守护进程
    #3. 启动进程
    p1.start()

    #4.主进程(main)休眠1秒后,结束
    time.sleep(1)

    #思路2: 强制关闭子进程
    # p1.terminate()
    print("main进程结束了")

