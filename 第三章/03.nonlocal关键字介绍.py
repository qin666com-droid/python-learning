"""
案例: nonlocal关键字介绍

nonlocal:
    它是python内置的关键字,可以实现 在内部函数中
    修改外部函数的 变量值

"""
#需求:编写一个闭包,让内部函数访问外部函数的参数 a=100,并观察结果

def fun_out():
    a = 100
    def fun_in():
        nonlocal a # nonlocal 可以实现内部函数中修改外部函数的变量值
        a += 10
        print(a)
    return fun_in

if __name__ == '__main__':
    fun_in= fun_out()
    fun_in()
    fun_in()
    fun_in()