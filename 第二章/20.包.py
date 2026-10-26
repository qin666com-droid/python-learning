#1. 导入模块
# import utils.my_fun
#
#
# utils.my_fun.log1()

# from utils import my_fun
#
# my_fun.log1()
# my_fun.log2()
# my_fun.log3()

#注意:如果要通过from utils import * 导入包下的所有模块
#              需要__init__.py 文件中添加 __all__ =[]
#
# from utils import *
# my_fun.log1()
# my_fun.log2()
# 2. 导入模块中的功能
#相对路径:从当前文件所在目录开始查找
from utils.my_fun import log1,log2

#绝对路径:从项目的根目录下开始查找
from 第二章.utils.my_fun import log3

log2()
log1()
log3()
