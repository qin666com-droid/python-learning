"""
案例 : 演示多线程共享全局变量,可能出现的问题

多线程共享全局变量,出现问题的问题:
    累加次数不够
产生原因:
    线程1还没来得及执行完(一个完整的动作)前,被线程2抢走了资源,就可能出问题
解决方案:
    加锁思想,即: 互斥锁

细节:
    使用互斥锁的时候,要在合适的时机释放锁,否则会导致 死锁 或者 锁不住 的情况


进程与线程的区别:
    1.线程依赖进程,进程是CPU分配资源的基本单位,线程是CPU调度资源的基本单位
    2.进程更消耗资源,不能共享全局变量,相对更稳定
    3.线程更轻量级,可以共享全局变量,相对更灵活
"""
#需求: 定义两个函数,分别对全局变量累加100w次,创建两个线程,关联两个线程,执行看结果
import threading,time
#1.定义全局变量
my_num = 0
#创建线程锁
lock = threading.Lock()
#2.定义目标函数,实现累加100w次
def add_100w():
    #加锁
    lock.acquire()
    global my_num
    #累加100w次
    for i in range(1000000):
        my_num += 1
    print(f"add_100w函数:{my_num}")
    #解锁
    lock.release()
#3.定义目标函数2,对全局变量累加100w次
def add_100w_2():
    global my_num
    lock.acquire()
    #累加100w次
    for i in range(1000000):
        my_num += 1
    print(f"add_100w_2函数:{my_num}")
    #解锁
    lock.release()
#4.测试
if __name__ == "__main__":
    #4.1 创建线程对象
    t1 = threading.Thread(target=add_100w)
    t2 = threading.Thread(target=add_100w_2)
    #4.2 启动线程
    t1.start()
    t2.start()




