#读文件
"""
路径写法:
    相对路径: 从当前文件所在目录开始查找文件(推荐)
        . : 表示当前目录 --->../recources/静夜思.txt   ./ 可以省略
        .. : 表示上一级目录 --->../第三章/data/my.txt
    绝对路径: 从根目录开始查找文件,文件位置的完整路径,包含文件名和扩展名
            注意: \ 在字符串中需要转义,所以需要使用 \\ 表示一个反斜杠
        / : 表示根目录 --->/AI--第一章/02.文件操作扩展.py



"""


with open("../第三章/data/my.txt", 'r',encoding='utf-8') as f:
    content = f.read()
    print(content)



#写文件
# a: append,追加写入;w: write,覆盖写入  --->文件不存在时,会创建新文件
# with open("recources/春江秋月夜.txt", 'a',encoding='utf-8') as f:
#     f.write("春江秋月夜(小鲸鱼)\n")
#     f.write("春江秋月夜,月明人影斜\n")

with open("recources/春江秋月夜.txt", 'a',encoding='utf-8') as f:
    f.write("独立寒堤风满袖，一江流梦到天涯\n")






