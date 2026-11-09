#1.导入线程模块
import threading

def coding(num,name):
    for i in range(1,num+1):
        print(f"{name}正在写第{i}行代码")

def music(num,name):
    for i in range(1,num+1):
        print(f"{name}正在听第{i}首音乐")

if __name__ == '__main__':
    #1.创建线程对象
    t1 = threading.Thread(target=coding,args=(5,"张三"))
    t2 = threading.Thread(target=music,args=(10,"李四"))
    #2.启动线程
    t1.start()
    t2.start()