"""
案例: 演示多线程的特点-随机性

多线程特点:
    1. 线程执行具有随机性,原因是因为CPU在做着高效的多线程切换
    2. 默认情况下,主线程会等待子线程结束再结束
    3.(同一个进程的)线程间 数据共享
    4. 多线程操作共享数据, 可能会出现安全问题,可以用 互斥锁解决

CPU调度资源的策略:
    1.均分时间片
    2.抢占式调度

"""
#需求: 创建多个线程,多次运行,观察结果
#导包
import threading
import time
from threading import current_thread


#1.定义对线程的目标函数
def print_onfo():
    #1.1休眠
    time.sleep(0.2)
    #1,2 获取当前进程对象
    current_thread = threading.current_thread()
    #1.3 打印当前进程对象
    print(current_thread.name)

#测试
if __name__ == '__main__':
    #2.1 创建线程
    for i in  range(10):
        t = threading.Thread(target=print_onfo)
        t.start()
