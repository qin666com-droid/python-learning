"""
案例: 正则替换的演示

回顾正则的使用方式:
    1. 导包
        import re
    2. 正则匹配
        result = re.match(正则表达式,字符串)    从前向后匹配,只要能匹配即可
        result = re.search(正则表达式,字符串)    分段匹配,只要能匹配即可,就返回第一个匹配结果
        result = re.compile(正则表达式).sub(替换字符串,字符串)    替换字符串
    3. 获取匹配结果
        result.group()


"""

# 导包
import re
from unittest import result

#1.定义字符串
s = '开心就大笑,哈哈哈,嘿嘿嘿,呵呵呵,啦啦啦,桀桀桀,咯咯咯,鹅鹅鹅'

#2. 把上述的 哈,嘿,呵,替换成♥
#                   正则规则         新字符串     被替换的字符串
result = re.compile('哈|嘿|呵|咯').sub('♥',s)
#3. 打印结果
print(result)

print('*'*30)

#新版API 的写法
#参1: 正则表达式  参2: 新字符串  参3: 被替换的字符串
result = re.sub('哈|嘿|呵|咯','♣',s)
print(result)
